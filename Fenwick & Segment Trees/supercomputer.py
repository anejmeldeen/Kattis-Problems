import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

bit = [0] * (n + 1)
def add(idx, val):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx
def query(idx):
    total = 0
    while idx > 0:
        total += bit[idx]
        idx -= idx & -idx
    return total

arr = [0] * (n + 1)

res = []
for _ in range(k):
    data = input().split()
    if data[0] == "F":
        idx = int(data[1])
        if arr[idx] == 1:
            arr[idx] = 0
            add(idx, -1)
        else:
            arr[idx] = 1
            add(idx, 1)
    else:
        left = int(data[1])
        right = int(data[2])
        res.append(query(right) - query(left - 1))

print("\n".join(list(map(str, res))))