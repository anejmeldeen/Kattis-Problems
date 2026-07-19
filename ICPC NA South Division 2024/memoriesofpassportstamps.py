import math
from fractions import Fraction

n, k = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(int(input()))

def check_val(x):
    count = 0
    for ele in arr:
        count += (ele + x - 1) // x
    return count

best = float('inf')
left = 1
right = max(arr)
while left <= right:
    mid = left + (right - left) // 2
    count = check_val(mid)
    if count > k:
        left = mid + 1
    else:
        best = mid
        right = mid - 1

print(best)