"""Validate sample answers, generated input bounds, and runner failure detection."""
import itertools
import math
from pathlib import Path
import random
import sys
import tempfile
import cases as c
import runner

def sample_answer(problem,data):
    tokens=iter(data.split()); num=lambda:int(next(tokens))
    if problem=='A':
        n,L=num(),num(); sp=used=0
        for _ in range(n):
            a,q=num(),num(); sp+=(q+L//a-1)//(L//a); used+=a*q
        return f'{sp} {sp*L-used}'
    if problem=='C':
        words=[next(tokens) for _ in range(num())]
        return str(sum(c.palette(a,b) for a,b in itertools.combinations(words,2)))
    if problem=='D':
        result=[]
        for _ in range(num()):
            R,P,Q,L,U=[num() for _ in range(5)]
            roots=[b for b in range(L,U+1) if Q*(R*(R-1)+b*(b-1))==P*(R+b)*(R+b-1)]
            result.append(' '.join(map(str,[len(roots),*roots])))
        return '\n'.join(result)
    if problem=='E':
        n,q=num(),num(); a=[num() for _ in range(n)]; result=[]
        for _ in range(q):
            l,r=num(),num(); result.append(sum(v==2 for v in c.Counter(a[l-1:r]).values()))
        return '\n'.join(map(str,result))
    if problem=='F':
        n,m,C,s,t=[num() for _ in range(5)]; fees=[num() for _ in range(n)]; edges=[]
        for _ in range(m):
            u,v,w,k=[num() for _ in range(4)]; edges.append((u-1,v-1,w,k))
        return str(c.freight(n,fees,edges,s-1,t-1))
    if problem=='G':
        n,a=num(),num(); p=[(num(),num()) for _ in range(n)]
        return str(c.gallery(p,a))
    if problem=='H': return '\n'.join(str(c.hues(num(),num())) for _ in range(num()))
    if problem=='I':
        n,b,m=num(),num(),num(); jobs=[tuple(num() for _ in range(3)) for _ in range(n)]
        blackouts=[(num(),num()) for _ in range(b)]
        return str(c.schedule(jobs,blackouts,m))
    if problem=='J':
        n,C,s,t=[num() for _ in range(4)]; cards=[]
        for _ in range(n):
            a,b,cost,p=[num() for _ in range(4)]; cards.append((a,b,cost,[num()-1 for _ in range(p)]))
        return str(c.exhibits(cards,s,t))
    if problem=='K':
        n,m,h=[num() for _ in range(3)]; costs=[(num(),num()) for _ in range(n)]; fees=[]; rest=[]
        for _ in range(m): fees.append((num()-1,num()-1,num()))
        for _ in range(h): rest.append((num()-1,num()-1))
        return str(c.peace(costs,fees,rest))
    if problem=='L': return '\n'.join(str(c.echoes(next(tokens))) for _ in range(num()))

def main():
    checked=0
    for p, samples in c.SAMPLES.items():
        for data,answer in samples:
            got=sample_answer(p,data)
            assert runner.matches(p,answer,got),(p,answer,got)
            checked+=1
    # Cross-check fixed adversarial cases, except algebra cases with enormous bounds.
    for p in c.SAMPLES:
        if p=='D': continue
        for name,data,expected in c.fixed(p):
            assert runner.matches(p,expected,sample_answer(p,data)),(p,name)
            checked+=1
    # Large-case formulas checked against small brute-force versions.
    for period in range(1,9):
        a=[i%period for i in range(40)]
        for l in range(40):
            for r in range(l+1,41):
                base,extra=divmod(r-l,period)
                fast=extra if base==1 else period-extra if base==2 else 0
                assert fast==sum(v==2 for v in c.Counter(a[l:r]).values())
                checked+=1
    # Verify a valid interactive binary search, plus rejection of wrong answers,
    # query overflow, bad ranges, extra output, and missing flush.
    good='''import sys
n=int(input())
found=[]
def search(l,r,k):
    if not k:return
    if r-l+1==k:found.extend(range(l,r+1));return
    mid=(l+r)//2
    print('?',l,mid,flush=True)
    v=int(input())
    search(l,mid,v);search(mid+1,r,k-v)
search(1,n,2)
print('!',*sorted(found),flush=True)
'''
    with tempfile.TemporaryDirectory() as folder:
        path=Path(folder)/'submission.py'; path.write_text(good)
        for n,a,b in runner.bell_cases(random.Random(1),20,True):
            ok,_,q,log=runner.interactive([sys.executable,str(path)],n,a,b,2)
            assert ok and q<=40,log
            checked+=1
        bads=["input(); print('! 1 2',flush=True)",
              "input(); print('? 0 1',flush=True)",
              "input()\nfor _ in range(41):\n print('? 1 1',flush=True); input()",
              "input(); print('! 3 7',flush=True); print('extra',flush=True)",
              "input(); print('? 1 4'); input()"]
        for code in bads:
            path.write_text(code)
            ok,_,_,_=runner.interactive([sys.executable,str(path)],8,3,7,.3)
            assert not ok,code
            checked+=1
        path.write_text('import time; time.sleep(2)')
        assert runner.batch([sys.executable,str(path)],'',.1)[0]=='TIMEOUT'
        path.write_text("raise SystemExit(7)")
        assert runner.batch([sys.executable,str(path)],'',1)[0]=='EXIT 7'
        assert not runner.matches('G','1','nan')
        assert not runner.matches('A','1','1 extra')
        assert not runner.matches('A','1','1.0')
        checked+=5
    # Exercise every random and maximum-size generator and verify total budgets.
    for p in c.SAMPLES:
        for name,data,answer in itertools.chain(c.small(p,random.Random(2026),8),c.stress(p)):
            assert data.endswith('\n') and answer.strip(),(p,name)
            lines=data.splitlines()
            if p=='H':
                pairs=[tuple(map(int,x.split())) for x in lines[1:]]
                assert len(pairs)<=50 and sum(n*(k+1) for n,k in pairs)<=400000
            if p=='L':
                assert max(map(len,lines[1:]))<=250 and sum(len(s)**3 for s in lines[1:])<=250**3
            if p=='C': assert sum(map(len,lines[1:]))<=200000
            if p=='G':
                points=[tuple(map(int,s.split())) for s in lines[1:]]
                turns=[]
                for i,b in enumerate(points):
                    a=points[i-1]; d=points[(i+1)%len(points)]
                    turns.append((b[0]-a[0])*(d[1]-b[1])-(b[1]-a[1])*(d[0]-b[0]))
                assert all(t>0 for t in turns) or all(t<0 for t in turns)
                assert max(abs(x) for v in points for x in v)<=10**9
            checked+=1
    print(f'Self-check passed: {checked} checks; all booklet samples and every generator exercised.')

if __name__=='__main__': main()
