import sys
import subprocess

def run_judge():
    if len(sys.argv) < 2:
        print("Usage: python3 judge_A.py <your_command>")
        return

    # Hidden Truth: N = 100000, Peak is at 74321
    N = 100000
    peak_idx = 74321
    
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
            if queries > 50:
                print(f"WRONG ANSWER: Exceeded 50 queries (Used {queries})")
                process.kill()
                return
                
            _, x_str = line.split()
            x = int(x_str)
            
            # The depth function: drops off by 1 for each sector away from the peak
            depth = 1000000 - abs(peak_idx - x)
            process.stdin.write(f"{depth}\n")
            process.stdin.flush()
            
        elif line.startswith("!"):
            _, ans_str = line.split()
            ans = int(ans_str)
            if ans == peak_idx:
                print(f"ACCEPTED: Found peak {peak_idx} in {queries} queries!")
            else:
                print(f"WRONG ANSWER: Guessed {ans}, actual peak was {peak_idx}")
            process.kill()
            return

if __name__ == '__main__':
    run_judge()