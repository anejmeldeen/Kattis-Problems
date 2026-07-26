n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

total_len = n * 3

bit = [0] * (total_len + 1)
def add(idx, val):
    while idx <= total_len:
        bit[idx] += val
        idx += idx & -idx
def query(idx):
    total = 0
    while idx > 0:
        total += bit[idx]
        idx -= idx & -idx
    return total

mappy = {}
for i, ele in enumerate(arr):
    add(i + n + 1, 1)
    mappy[ele] = i + n + 1

lefty = n
righty = 2 * n + 1
low = 1
high = n
left = True
while low <= high:
    if left:
        print(query(mappy[low]) - low)
        add(mappy[low], -1)
        add(lefty, 1)
        lefty -= 1
        low += 1
    else:
        print(high - query(mappy[high]))
        add(mappy[high], -1)
        add(righty, 1)
        righty += 1
        high -= 1
    left = not left