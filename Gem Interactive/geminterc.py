import sys

n = int(input())

start = 1
best = 0
cand = -1
for i in range(2, n + 1):
    print(f"? {start} {i}")
    sys.stdout.flush()

    val = int(input())
    if val > best:
        best = val
        cand = i

start = cand
best = 0
cand = -1
for i in range(1, n + 1):
    if i == start:
        continue

    print(f"? {start} {i}")
    sys.stdout.flush()

    val = int(input())
    if val > best:
        best = val
        cand = i

print(f"! {start} {cand}")