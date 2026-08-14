h = list(map(int, input().split()))
b = list(map(int, input().split()))
h = h[1:]
b = b[1:]
h.sort()
b.sort()

def can_sum(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i, num in enumerate(arr):
        

for target in range(1, 1000001):
    if can_sum(h, target) and can_sum(b, target):
        print(target)   