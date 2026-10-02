from bisect import bisect_right
n, t, k = list(map(int, input().split()))

meetings = []
for _ in range(n):
    s, e = list(map(int, input().split()))
    meetings.append((s, e))
meetings.sort(key=lambda x: x[1])
ends = [x[1] for x in meetings]

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[0][i] = float('inf')

for i in range(1, n + 1):
    start, end = meetings[i - 1]
    length = end - start
    compatible_idx = bisect_right(ends, start)
    for j in range(1, n + 1):
        dp[i][j] = min(dp[compatible_idx][j - 1] + length, dp[i - 1][j])

for j in range(n, -1, -1):
    for i in range(n + 1):
        if dp[i][j] <= t - k:
            print(j)
            exit()