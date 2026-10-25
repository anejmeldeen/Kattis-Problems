import sys
import subprocess
from collections import deque

def run_judge():
    if len(sys.argv) < 2:
        print("Usage: python3 judge_A_courier.py <your_command>")
        return

    # Hidden Truth: N = 2000
    # We construct a tree with a single unique longest path (diameter)
    N = 2000
    adj = {i: [] for i in range(1, N + 1)}
    
    # Build a main path from 1 to 1000 (Length = 999)
    for i in range(1, 1000):
        adj[i].append(i + 1)
        adj[i + 1].append(i)
    
    # Attach the remaining 1000 nodes to the midpoint (node 500) as short branches
    for i in range(1001, N + 1):
        adj[500].append(i)
        adj[i].append(500)

    # The only true endpoints of the maximum diameter are 1 and 1000
    valid_endpoints = {1, 1000}
    max_dist = 999

    def get_dist(u, v):
        q = deque([(u, 0)])
        visited = {u}
        while q:
            curr, dist = q.popleft()
            if curr == v:
                return dist
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
        return -1

    process = subprocess.Popen(sys.argv[1:], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    # Send N
    process.stdin.write(f"{N}\n")
    process.stdin.flush()

    queries = 0
    while True:
        line = process.stdout.readline().strip()
        if not line: break
        
        if line.startswith("?"):
            queries += 1
            if queries > 2 * N:
                print(f"WRONG ANSWER: Exceeded 2N queries (Used {queries})")
                process.stdin.write("-1\n")
                process.stdin.flush()
                process.kill()
                return
                
            _, u_str, v_str = line.split()
            u, v = int(u_str), int(v_str)
            
            dist = get_dist(u, v)
            process.stdin.write(f"{dist}\n")
            process.stdin.flush()
            
        elif line.startswith("!"):
            _, a_str, b_str = line.split()
            a, b = int(a_str), int(b_str)
            
            if {a, b} == valid_endpoints:
                print(f"ACCEPTED: Found endpoints {a} and {b} in {queries} queries!")
            else:
                actual_d = get_dist(a, b)
                print(f"WRONG ANSWER: Guessed {a} and {b} (distance {actual_d}). True diameter is {max_dist}.")
            process.kill()
            return

if __name__ == '__main__':
    run_judge()