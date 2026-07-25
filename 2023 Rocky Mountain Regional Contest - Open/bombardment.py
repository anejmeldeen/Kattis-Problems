from bisect import bisect_left

n, r = list(map(int, input().split()))
arr = list(map(int, input().split()))
counts = {}
arr.sort()

sol = []
while arr:
    best_count = 0
    best_spot = -1
    left_affect = -1
    right_affect = -1
    for right, num in enumerate(arr):
        low = num - r * 2
        idx = bisect_left(arr, low)
        if right - idx + 1 > best_count:
            best_count = right - idx + 1
            best_spot = num
            left_affect = idx
            right_affect = right
    sol.append(best_spot - r)
    arr = arr[:left_affect] + arr[right_affect + 1:]

print(len(sol))
print(' '.join(list(map(str, sol))))