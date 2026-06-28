n = int(input())
intervals = []
for _ in range(n):
    d, r = list(map(int, input().split()))
    intervals.append((d, r))

dp = [1] * n
for i, interval in enumerate(intervals):
    d, r = interval
    for j in range(i):
        prev_d, prev_r = intervals[j]
        if d - r > prev_d and prev_d + prev_r < d:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))