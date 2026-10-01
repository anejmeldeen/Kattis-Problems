import math

m = int(input())
arr = []

for _ in range(m):
    arr.append(int(input()))

counts = {}
for ele in arr:
    counts[ele] = counts.get(ele, 0) + 1

maxi = 1
for key in counts:
    count = counts[key]
    curr = key + 1
    amount = curr
    diff = amount - count
    remove = diff // 2
    maxi = max(maxi, curr - remove)

print(maxi)