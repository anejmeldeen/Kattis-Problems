"""Test generation and independent small-instance oracles. Contains spoilers."""
import itertools as it
import math
import random
from collections import Counter
from functools import lru_cache

MOD = 1000000007

def pack(rows):
    return '\n'.join(' '.join(map(str, r)) if not isinstance(r, str) else r for r in rows) + '\n'

def case(name, rows, answer):
    return name, pack(rows), str(answer)

def palette(s, t):
    if len(s) != len(t): return False
    def oriented(t):
        f, g = {}, {}
        for a, b in zip(s, t):
            if a in f and f[a] != b or b in g and g[b] != a: return False
            f[a], g[b] = b, a
        return True
    return oriented(t) or oriented(t[::-1])

def freight(n, fees, edges, s, t):
    # Bellman-Ford on an explicit state graph (independent of Dijkstra).
    colors = set(e[3] for e in edges)
    states = [(u,c,r,v) for u in range(n) for c in colors for r in (1,2) for v in (0,1)]
    start = (s,0,0,0)
    dist = {start: 0}
    for _ in range(len(states)+1):
        changed = False
        for state, d in list(dist.items()):
            u,c,r,v = state
            for a,b,w,k in edges:
                if a != u or c == k and r == 2: continue
                rr = r+1 if c == k else 1
                fee = fees[u] if c and c != k else 0
                options = [(v,fee)]
                if not v and c and c != k: options.append((1,0))
                for vv, charge in options:
                    nxt = (b,k,rr,vv)
                    nd = d+w+charge
                    if nd < dist.get(nxt,math.inf):
                        dist[nxt] = nd; changed = True
        if not changed: break
    ans = min((d for st,d in dist.items() if st[0] == t),default=math.inf)
    return 'impossible' if ans == math.inf else ans

def area(p):
    return abs(sum(x*v-y*u for (x,y),(u,v) in zip(p,p[1:]+p[:1])))

def perimeter(p):
    return sum(math.hypot(x-u,y-v) for (x,y),(u,v) in zip(p,p[1:]+p[:1]))

def gallery(p, threshold):
    n=len(p); best=perimeter(p)
    for count in (1,2):
        for deleted in it.combinations(range(n),count):
            if count == 2 and (deleted[1]-deleted[0] in (1,n-1)): continue
            q=[v for i,v in enumerate(p) if i not in deleted]
            if area(q)>=threshold: best=min(best,perimeter(q))
    return best

def hues(n,k):
    # Recursive exhaustive coloring enumeration for small tests.
    result=0
    def visit(seq, matches):
        nonlocal result
        if matches>k: return
        if len(seq)==n:
            result += matches==k and seq[-1]!=seq[0]
            return
        i=len(seq)
        for c in range(3):
            if not seq or c!=seq[-1]: visit(seq+[c],matches+(c==i%3))
    visit([],0)
    return result

def schedule(jobs, blackouts, allowed):
    active=[d-sum(max(0,min(d,r)-l) for l,r in blackouts if l<d) for _,d,_ in jobs]
    best=math.inf
    for mask in range(1<<len(jobs)):
        if len(jobs)-mask.bit_count()>allowed: continue
        if any(req and not(mask>>i&1) for i,(_,_,req) in enumerate(jobs)): continue
        pages=0; speed=1
        for i in sorted(range(len(jobs)),key=lambda i:jobs[i][1]):
            if not(mask>>i&1): continue
            pages+=jobs[i][0]
            if not active[i]: speed=math.inf; break
            speed=max(speed,(pages+active[i]-1)//active[i])
        best=min(best,speed)
    return 'impossible' if best==math.inf else best

def exhibits(cards,s,t):
    # Enumerate valid orderings and orientations, no memoization.
    best=math.inf; n=len(cards)
    def visit(mask,color,cost):
        nonlocal best
        if cost>=best: return
        if mask==(1<<n)-1:
            if color==t: best=cost
            return
        for i,(a,b,c,pre) in enumerate(cards):
            if mask>>i&1 or any(not(mask>>j&1) for j in pre): continue
            if a==color: visit(mask|1<<i,b,cost)
            if b==color: visit(mask|1<<i,a,cost+c)
    visit(0,s,0)
    return 'impossible' if best==math.inf else best

def peace(costs,fees,restrictions):
    best=math.inf
    for bits in it.product((0,1),repeat=len(costs)):
        if any(costs[i][b]<0 for i,b in enumerate(bits)): continue
        if any(bits[u]==0 and bits[v]==1 for u,v in restrictions): continue
        total=sum(costs[i][b] for i,b in enumerate(bits))
        total+=sum(c for u,v,c in fees if bits[u]==0 and bits[v]==1)
        best=min(best,total)
    return 'impossible' if best==math.inf else best

@lru_cache(None)
def echoes(s):
    # Direct grammar recurrence on substrings, without LCP/palindrome tables.
    n=len(s); best=n
    for i in range(1,n): best=min(best,echoes(s[:i])+echoes(s[i:]))
    for p in range(1,n):
        if n%p==0 and s[:p]*(n//p)==s: best=min(best,len(str(n//p))+2+echoes(s[:p]))
    if n>=2 and s==s[::-1]: best=min(best,(2 if n%2==0 else 4)+echoes(s[:n//2]))
    return best

def small(problem, rng, count):
    for z in range(count):
        label=f'random-{z:04d}'
        if problem=='A':
            L=rng.randint(1,30); orders=[(rng.randint(1,L),rng.randint(1,80)) for _ in range(rng.randint(1,12))]
            spools=returned=0
            for a,q in orders:
                # Simulate filling and purchasing individual spools.
                left=0
                for _ in range(q):
                    if left<a:
                        returned+=left; spools+=1; left=L
                    left-=a
                returned+=left
            yield case(label,[(len(orders),L),*orders],f'{spools} {returned}')
        elif problem=='C':
            words=[''.join(rng.choices('abcd',k=rng.randint(1,9))) for _ in range(rng.randint(1,25))]
            if z%2==0: words+=words[:3]+[s[::-1] for s in words[:3]]
            ans=sum(palette(a,b) for a,b in it.combinations(words,2))
            yield case(label,[(len(words),),*words],ans)
        elif problem=='D':
            rows=[]; answers=[]
            for _ in range(15):
                R=rng.randint(1,30); Q=rng.randint(1,100); P=rng.randint(0,Q); lo=rng.randint(1,20); hi=rng.randint(lo,100)
                if rng.random()<.6:
                    B=rng.randint(lo,hi); P=R*(R-1)+B*(B-1); Q=(R+B)*(R+B-1)
                values=[b for b in range(lo,hi+1) if Q*(R*(R-1)+b*(b-1))==P*(R+b)*(R+b-1)]
                rows.append((R,P,Q,lo,hi)); answers.append(' '.join(map(str,[len(values),*values])))
            yield case(label,[(len(rows),),*rows],'\n'.join(answers))
        elif problem=='E':
            n=rng.randint(1,35); a=[rng.choice([1,2,3,4,10**9]) for _ in range(n)]
            queries=[(l,r) for l in range(1,n+1) for r in range(l,n+1)]
            rng.shuffle(queries)
            ans=[sum(v==2 for v in Counter(a[l-1:r]).values()) for l,r in queries]
            yield case(label,[(n,len(queries)),a,*queries],'\n'.join(map(str,ans)))
        elif problem=='F':
            n=rng.randint(2,6); C=rng.randint(1,4); s=rng.randrange(n); t=rng.randrange(n)
            fees=[rng.choice([0,1,10,10**6]) for _ in range(n)]; edges=[]
            for _ in range(rng.randint(0,20)):
                u,v=rng.sample(range(n),2); edges.append((u,v,rng.randint(1,20),rng.randint(1,C)))
            yield case(label,[(n,len(edges),C,s+1,t+1),fees,*[(u+1,v+1,w,c) for u,v,w,c in edges]],freight(n,fees,edges,s,t))
        elif problem=='G':
            # Points on a parabola plus closing chord form a strictly convex polygon.
            xs=sorted(rng.sample(range(-30,31),rng.randint(6,12)))
            p=[(x,x*x) for x in xs]
            if z%2: p.reverse()
            factor=rng.choice([1,1,10**6]); p=[(x*factor,y*factor) for x,y in p]
            threshold=rng.choice([0,area(p),rng.randrange(area(p)+1)])
            yield case(label,[(len(p),threshold),*p],gallery(p,threshold))
        elif problem=='H':
            pairs=[(n,k) for n in range(2,10) for k in range(n+1)] if z==0 else [(rng.randint(2,11),rng.randint(0,11)) for _ in range(10)]
            pairs=[(n,min(n,k)) for n,k in pairs][:50]
            yield case(label,[(len(pairs),),*pairs],'\n'.join(str(hues(n,k)) for n,k in pairs))
        elif problem=='I':
            n=rng.randint(1,9); m=rng.randrange(n)
            jobs=[(rng.randint(1,30),rng.randint(1,20),rng.randrange(2)) for _ in range(n)]
            points=sorted(rng.sample(range(22),2*rng.randint(0,5))); blackouts=list(zip(points[::2],points[1::2]))
            yield case(label,[(n,len(blackouts),m),*jobs,*blackouts],schedule(jobs,blackouts,m))
        elif problem=='J':
            n=rng.randint(1,7); C=rng.randint(2,4); s=rng.randint(1,C); t=rng.randint(1,C); cards=[]
            for i in range(n):
                a,b=rng.sample(range(1,C+1),2)
                pre=[j for j in range(n) if j!=i and rng.random()<.12]
                cards.append((a,b,rng.choice([0,1,10**9]),pre))
            rows=[(a,b,c,len(pre),*[j+1 for j in pre]) for a,b,c,pre in cards]
            yield case(label,[(n,C,s,t),*rows],exhibits(cards,s,t))
        elif problem=='K':
            n=rng.randint(1,10); costs=[(rng.choice([-1,0,3,10**9]),rng.choice([-1,0,7,10**9])) for _ in range(n)]
            fees=[]; rest=[]
            if n>1:
                for _ in range(rng.randint(0,20)):
                    u,v=rng.sample(range(n),2); fees.append((u,v,rng.choice([0,1,10**9])))
                for _ in range(rng.randint(0,10)): rest.append(tuple(rng.sample(range(n),2)))
            yield case(label,[(n,len(fees),len(rest)),*costs,*[(u+1,v+1,c) for u,v,c in fees],*[(u+1,v+1) for u,v in rest]],peace(costs,fees,rest))
        elif problem=='L':
            strings=[''.join(rng.choices('ABC',k=rng.randint(1,16))) for _ in range(10)]
            base=''.join(rng.choices('ABC',k=rng.randint(1,6)))
            strings += [base*6,base+base[::-1],base+'Z'+base[::-1]]
            yield case(label,[(len(strings),),*strings],'\n'.join(str(echoes(s)) for s in strings))

SAMPLES={
'A': [('3 10\n3 5\n6 2\n10 1\n','5 13')],
'C': [('6\nabac\nxyxz\ncaba\naaaa\nbbbb\nabca\n','4')],
'D': [('3\n2 1 3 1 10\n1 0 1 1 10\n3 1 1 1 100\n','2 1 2\n1 1\n0')],
'E': [('6 5\n1 2 1 2 1 3\n1 4\n1 5\n2 5\n3 6\n1 1\n','2\n1\n2\n1\n0')],
'F': [('4 5 2 1 4\n0 10 5 0\n1 2 3 1\n2 3 1 1\n3 4 1 1\n2 4 8 2\n1 3 7 2\n','8')],
'G': [('6 12\n0 0\n2 0\n3 1\n2 3\n0 3\n-1 1\n','10')],
'H': [('3\n3 3\n3 0\n2 0\n','1\n2\n3')],
'I': [('3 1 1\n4 4 1\n3 5 0\n3 6 0\n1 3\n','2'),('1 1 0\n1 4 1\n0 5\n','impossible')],
'J': [('3 3 1 2\n1 2 5 0\n3 2 2 1 1\n3 2 4 1 2\n','2')],
'K': [('3 2 1\n0 7\n8 0\n0 5\n1 2 4\n3 2 3\n1 3\n','7')],
'L': [('4\nAAAAAA\nABABABABABAB\nABCDDCBA\nABCDEZEDCBA\n','4\n5\n6\n9')]
}

def fixed(p):
    for i,(data,answer) in enumerate(SAMPLES[p]): yield f'sample-{i+1}',data,answer
    if p=='A':
        yield case('indivisible-pieces',[(2,10),(6,3),(6,3)],'6 24')
    if p=='C':
        words=['a','b','aa','ab','aba','abc','abac','caba','abca','xyxz']
        yield case('bijection-reversal',[(len(words),),*words],sum(palette(a,b) for a,b in it.combinations(words,2)))
    if p=='D':
        yield case('huge-bounds',[(4,),(1,0,1000000000,1,10**18),(1,1,1,1,10**18),(2,1,3,2,2),(2,1,3,3,10**18)],'1 1\n0\n1 2\n0')
        # R=1 => probability=(B-1)/(B+1); exact large root.
        yield case('large-root',[(1,),(1,499999999,500000000,1,10**18)],'1 999999999')
    if p=='F':
        yield case('voucher-cannot-reset-run',[(4,3,1,1,4),(0,99,99,0),(1,2,1,1),(2,3,1,1),(3,4,1,1)],'impossible')
        yield case('empty-trip',[(2,0,1,1,1),(0,0)],0)
    if p=='I':
        jobs=[(4,2,0),(4,4,0),(20,5,1)]
        yield case('required-forces-multiple-deletions',[(3,0,2),*jobs],schedule(jobs,[],2))
        yield case('touching-blackouts',[(2,2,1),(1,4,0),(1,5,1),(0,2),(2,4)],1)
    if p=='J':
        yield case('prerequisite-cycle',[(2,2,1,1),(1,2,0,1,2),(2,1,0,1,1)],'impossible')
    if p=='K':
        yield case('both-forbidden',[(1,0,0),(-1,-1)],'impossible')
        yield case('directed-fee',[(2,1,0),(-1,0),(0,-1),(1,2,10**9)],0)
        yield case('duplicate-large-fees',[(2,3,0),(0,-1),(-1,0),(1,2,10**9),(1,2,10**9),(1,2,10**9)],3*10**9)
    if p=='L':
        strings=['A','AA','ABA','ABBA','A'*99,'A'*100,'AB'*50,'ABC'*30,'ABCCBA'*12]
        yield case('constructors-and-digit-boundaries',[(len(strings),),*strings],'\n'.join(str(echoes(s)) for s in strings))

def stress(p):
    """Increasing legal sizes. Expected results use constructions, not submissions."""
    if p=='A':
        for n in (1000,10000,100000):
            yield case(f'scale-{n}',[(n,1000000),*[(999999,1000000)]*n],f'{n*1000000} {n*1000000}')
    elif p=='C':
        for n in (2000,20000,200000):
            yield case(f'scale-{n}',[(n,),*['a']*n],n*(n-1)//2)
        s='abcdefghijklmnopqrstuvwxyz'*7692+'abcdefgh'
        yield case('one-long-label',[(1,),s],0)
    elif p=='D':
        yield case('maximum-T-and-bounds',[(1000,),*[(2,1,3,1,10**18)]*1000],'\n'.join(['2 1 2']*1000))
    elif p=='E':
        for n in (2000,20000,200000):
            queries=[(1,n)]*(n//2)+[(i,i) for i in range(1,n//2+1)]
            # Every identifier appears twice, one in each half.
            a=list(range(1,n//2+1))*2
            yield case(f'scale-{n}',[(n,n),a,*queries],'\n'.join(map(str,[n//2]*(n//2)+[0]*(n//2))))
        n=200000; rng=random.Random(971)
        queries=[]; ans=[]; period=137
        for _ in range(n):
            l=rng.randint(1,n); r=rng.randint(l,n); length=r-l+1
            base,extra=divmod(length,period)
            ans.append(extra if base==1 else period-extra if base==2 else 0)
            queries.append((l,r))
        yield case('periodic-random-query-order',[(n,n),[i%period+1 for i in range(n)],*queries],'\n'.join(map(str,ans)))
    elif p=='F':
        for n in (200,2000,20000):
            roads=[(i,i+1,w,1+i%2) for i in range(1,n) for w in (1,2,1000000)]
            yield case(f'scale-{n}',[(n,len(roads),2,1,n),[0]*n,*roads],n-1)
        n=20000; rng=random.Random(716)
        roads=[]
        for _ in range(60000):
            u,v=rng.sample(range(1,n),2); roads.append((u,v,rng.randint(1,10**6),rng.randint(1,4)))
        yield case('unreachable-dense-state-search',[(n,len(roads),4,1,n),[10**6]*n,*roads],'impossible')
    elif p=='G':
        for n in (100,500,2000):
            points=[(x,x*x) for x in range(-n//2,n//2)]
            yield case(f'scale-{n}-full-area',[(n,area(points)),*points],perimeter(points))
        points=[(x,x*x) for x in range(-1000,1000)]
        # Unrestricted area: independently combine the two greatest nonadjacent savings.
        n=len(points); savings=[]
        for i in range(n):
            a,b,c=points[i-1],points[i],points[(i+1)%n]
            savings.append(math.dist(a,b)+math.dist(b,c)-math.dist(a,c))
        best=max(savings)
        for i in range(n):
            for j in range(i+2,n):
                if i==0 and j==n-1: continue
                best=max(best,savings[i]+savings[j])
        yield case('scale-2000-zero-area',[(n,0),*points],perimeter(points)-best)
    elif p=='H':
        for n in (100,500,1990):
            k=200 if n>=200 else 99
            # Transfer-state counting oracle for large tests.
            total=0
            for first in range(3):
                dp={(first,int(first==0)):1}
                for i in range(1,n):
                    nxt={}
                    for (prev,matches),ways in dp.items():
                        for color in range(3):
                            kk=matches+(color==i%3)
                            if color!=prev and kk<=k:
                                key=(color,kk); nxt[key]=(nxt.get(key,0)+ways)%MOD
                    dp=nxt
                total+=sum(v for (last,kk),v in dp.items() if last!=first and kk==k)
            yield case(f'scale-{n}-k{k}',[(1,),(n,k)],total%MOD)
    elif p=='I':
        for n in (1000,10000,100000):
            jobs=[(10**9,200000,1)]*n
            blackouts=[(i,i+1) for i in range(n)]
            ans=(n*10**9+200000-n-1)//(200000-n)
            yield case(f'scale-{n}',[(n,n,0),*jobs,*blackouts],ans)
        n=100000
        # One giant required job forces deletion of every earlier optional job at v=1.
        jobs=[(1,100000,0)]*(n-1)+[(100001,100001,1)]
        yield case('large-optional-heap',[(n,0,n-1),*jobs],1)
    elif p=='J':
        for n in (10,13,16):
            yield case(f'scale-{n}',[(n,2,1,1+n%2),*[(1,2,0,0)]*n],0)
        yield case('large-flip-total',[(16,2,1,1),*[(2,1,10**9,1,i) if i else (2,1,10**9,0) for i in range(16)]],8*10**9)
    elif p=='K':
        for n in (50,200,500):
            rng=random.Random(786); fees=[]; rest=[]
            for _ in range(3000):
                u,v=rng.sample(range(1,n+1),2); fees.append((u,v,10**9))
                u,v=rng.sample(range(1,n+1),2); rest.append((u,v))
            # Every unary cost is 1: all-equal assignments attain the n lower bound.
            yield case(f'scale-{n}',[(n,3000,3000),*[(1,1)]*n,*fees,*rest],n)
    elif p=='L':
        rng=random.Random(916)
        for n in (50,125,250):
            s=''.join(rng.choices('ABCD',k=n))
            yield case(f'scale-{n}',[(1,),s],echoes(s))
        for label,s in [('uniform','A'*250),('periodic','ABCDE'*50),('mirror',('ABCD'*31+'A')+('ABCD'*31+'A')[::-1])]:
            yield case('max-'+label,[(1,),s],echoes(s))
