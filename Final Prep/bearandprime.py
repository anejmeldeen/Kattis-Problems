import sys
import math

n = int(input())

for _ in range(n):
    print("0 0")
    sys.stdout.flush()

    d = int(input())
    if d == 0:
        continue
    cands = []

    for x in range(0, 10 ** 6 + 1):
        y_sqr = d - x * x
        if y_sqr < 0:
            continue
        if int(math.sqrt(y_sqr)) ** 2 == y_sqr and int(math.sqrt(y_sqr)) <= 10 ** 6:
            cands.append((x, int(math.sqrt(y_sqr))))

    for cand in cands:
        print(f"{cand[0]} {cand[1]}")
        sys.stdout.flush()
        res = int(input())
        if res == 0:
            break