"""Shared batch and interactive execution. Python standard library only."""
import argparse
import itertools
import math
import os
from pathlib import Path
import random
import selectors
import shlex
import signal
import subprocess
import sys
import tempfile
import time
import cases

ROOT=Path(__file__).resolve().parent

def stop(proc):
    if proc.poll() is None:
        if os.name=='posix': os.killpg(proc.pid,signal.SIGKILL)
        else: proc.kill()
    proc.wait()

def command_for(args):
    if args.command: return shlex.split(args.command)
    if not args.solution: raise ValueError('provide a solution path or --command')
    path=Path(args.solution).resolve()
    if not path.is_file(): raise ValueError(f'file does not exist: {path}')
    return [sys.executable,str(path)] if path.suffix=='.py' else [str(path)]

def batch(cmd,data,timeout):
    # Files avoid pipe deadlocks and unbounded in-memory output capture.
    with tempfile.TemporaryFile() as inp, tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
        inp.write(data.encode()); inp.seek(0)
        start=time.perf_counter()
        proc=subprocess.Popen(cmd,stdin=inp,stdout=out,stderr=err,start_new_session=True)
        try: proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            stop(proc); return 'TIMEOUT',time.perf_counter()-start,'',f'exceeded {timeout:g}s'
        elapsed=time.perf_counter()-start
        if out.tell()>8*1024*1024: return 'OUTPUT LIMIT',elapsed,'','stdout exceeds 8 MiB'
        out.seek(0); output=out.read().decode('utf-8',errors='replace')
        err.seek(0); errors=err.read(4000).decode('utf-8',errors='replace')
        return ('OK' if proc.returncode==0 else f'EXIT {proc.returncode}'),elapsed,output,errors

def matches(problem,expected,actual):
    if problem=='G':
        tokens=actual.split()
        if len(tokens)!=1: return False
        try:
            a=float(tokens[0]); b=float(expected)
            return math.isfinite(a) and abs(a-b)<=1e-6*max(1,abs(b))
        except ValueError: return False
    # Parse numeric output as integers so 1.0 cannot silently pass an integer problem.
    def normalize(s):
        return [int(t) if t!='impossible' else t for t in s.split()]
    try: return normalize(expected)==normalize(actual)
    except ValueError: return False

def save_failure(problem,name,data,expected,actual,details,folder):
    folder=Path(folder)/problem; folder.mkdir(parents=True,exist_ok=True)
    prefix=folder/name
    prefix.with_suffix('.in').write_text(data)
    prefix.with_suffix('.expected').write_text(expected+'\n')
    prefix.with_suffix('.actual').write_text(actual)
    prefix.with_suffix('.error').write_text(details)
    return prefix.resolve()

def interactive(cmd,n,a,b,timeout):
    """Fixed hidden pair; strict line protocol and a total per-session deadline."""
    transcript=[f'judge: {n}']; queries=0; deadline=time.monotonic()+timeout
    with tempfile.TemporaryFile() as err:
        proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,start_new_session=True,bufsize=0)
        selector=selectors.DefaultSelector(); selector.register(proc.stdout,selectors.EVENT_READ)
        pending=b''
        def reply(value):
            proc.stdin.write((str(value)+'\n').encode()); proc.stdin.flush()
        def line():
            nonlocal pending
            while b'\n' not in pending:
                remaining=deadline-time.monotonic()
                if remaining<=0 or not selector.select(max(0,remaining)):
                    raise RuntimeError('TIMEOUT: waiting for a flushed protocol line')
                chunk=os.read(proc.stdout.fileno(),4096)
                if not chunk: raise RuntimeError('program exited before a complete final-answer line')
                pending+=chunk
                if len(pending)>4096: raise RuntimeError('protocol line too long')
            value,pending=pending.split(b'\n',1)
            return value.decode('ascii').strip()
        start=time.perf_counter()
        try:
            reply(n)
            while True:
                value=line(); transcript.append('program: '+value); parts=value.split()
                if len(parts)!=3 or parts[0] not in ('?','!'): raise RuntimeError('invalid protocol line')
                try: l,r=map(int,parts[1:])
                except ValueError: raise RuntimeError('non-integer protocol argument')
                if parts[0]=='?':
                    queries+=1
                    if queries>40: raise RuntimeError('query budget exceeded (40)')
                    if not 1<=l<=r<=n: raise RuntimeError('invalid interval')
                    answer=int(l<=a<=r)+int(l<=b<=r)
                    transcript.append('judge: '+str(answer)); reply(answer)
                else:
                    if (l,r)!=(a,b): raise RuntimeError(f'wrong pair; expected {a} {b}')
                    # A compliant submission terminates after the answer.
                    proc.stdin.close()
                    try: proc.wait(timeout=max(.001,deadline-time.monotonic()))
                    except subprocess.TimeoutExpired: raise RuntimeError('TIMEOUT: did not terminate after final answer')
                    tail=pending+proc.stdout.read(4096)
                    if tail.strip(): raise RuntimeError('extra stdout after final answer')
                    if proc.returncode: raise RuntimeError(f'nonzero exit: {proc.returncode}')
                    return True,time.perf_counter()-start,queries,'\n'.join(transcript)
        except (RuntimeError,BrokenPipeError,UnicodeError) as exc:
            transcript.append(str(exc))
            return False,time.perf_counter()-start,queries,'\n'.join(transcript)
        finally:
            stop(proc); selector.close()
            proc.stdout.close()
            if not proc.stdin.closed: proc.stdin.close()

def bell_cases(rng,count,large):
    for n in range(2,9):
        for a,b in itertools.combinations(range(1,n+1),2): yield n,a,b
    for _ in range(count):
        n=rng.randint(2,100000); a,b=sorted(rng.sample(range(1,n+1),2)); yield n,a,b
    if large:
        for n in (65535,65536,65537,99999,100000):
            for a,b in [(1,2),(1,n),(n-1,n),(n//2,n//2+1),(n//2-1,n//2)]: yield n,a,b

def main(problem):
    parser=argparse.ArgumentParser(description=f'Test a solution for problem {problem}.')
    parser.add_argument('solution',nargs='?',help='Python solution or executable path')
    parser.add_argument('--command',help='quoted command, e.g. "java -cp build Main"; no shell is used')
    parser.add_argument('--cases',type=int,default=60,help='random cases (default: 60)')
    parser.add_argument('--seed',type=int,default=2026)
    parser.add_argument('--timeout',type=float,default=15,help='seconds per process/session')
    parser.add_argument('--stress',action='store_true',help='include maximum-size and scaling tests')
    parser.add_argument('--stress-only',action='store_true',help='run only large scaling tests')
    parser.add_argument('--failures',default=str(ROOT/'failures'))
    args=parser.parse_args()
    if args.cases<0 or args.timeout<=0: parser.error('cases must be nonnegative; timeout must be positive')
    try: cmd=command_for(args)
    except ValueError as exc: parser.error(str(exc))
    rng=random.Random(args.seed); passed=0; slowest=(0,''); maximum_queries=0
    try:
        if problem=='B':
            tests=bell_cases(rng,0 if args.stress_only else args.cases,args.stress or args.stress_only)
            for n,a,b in tests:
                if args.stress_only and n<65535: continue
                name=f'n{n}-{a}-{b}'
                ok,elapsed,q,log=interactive(cmd,n,a,b,args.timeout)
                if not ok:
                    path=save_failure(problem,name,str(n)+'\n',f'! {a} {b}',log,'interactive failure',args.failures)
                    print(f'FAIL {name}; transcript: {path}.actual'); return 1
                maximum_queries=max(maximum_queries,q); passed+=1
                slowest=max(slowest,(elapsed,name))
            print(f'PASS B: {passed} sessions; maximum {maximum_queries}/40 queries; slowest {slowest[0]:.3f}s')
            return 0
        def tests():
            if not args.stress_only:
                yield from cases.fixed(problem)
                yield from cases.small(problem,rng,args.cases)
            if args.stress or args.stress_only: yield from cases.stress(problem)
        for name,data,expected in tests():
            status,elapsed,actual,err=batch(cmd,data,args.timeout)
            if status!='OK' or not matches(problem,expected,actual):
                path=save_failure(problem,name,data,expected,actual,status+'\n'+err,args.failures)
                print(f'FAIL {problem} {name}: {status if status!="OK" else "WRONG ANSWER"} ({elapsed:.3f}s)')
                print(f'Reproducer: {path}.in\nExpected: {expected[:300]}\nActual: {actual[:300]}')
                return 1
            passed+=1; slowest=max(slowest,(elapsed,name))
            if name.startswith(('scale-','max-')): print(f'  {name}: {elapsed:.3f}s',flush=True)
        print(f'PASS {problem}: {passed} cases; slowest {slowest[1]} at {slowest[0]:.3f}s; seed {args.seed}')
        return 0
    except (OSError,KeyboardInterrupt) as exc:
        print(f'Runner stopped: {exc}',file=sys.stderr); return 2
