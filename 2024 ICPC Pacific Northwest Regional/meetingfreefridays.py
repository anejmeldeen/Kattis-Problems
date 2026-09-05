from bisect import bisect_right

n, t, k = list(map(int, input().split()))
meetings = []
max_allowed = t - k

for _ in range(n):
    start, end = list(map(int, input().split()))
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))
ends = [x[1] for x in meetings]

prev = []
for i in range(n):
    prev.append(bisect_right(ends, meetings[i][0]))

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 0

for i in range(n):
    j = prev[i]
    row = dp[j]
    len_meeting = meetings[i][1] - meetings[i][0]
    for k in range(1, n + 1):
        dp[i + 1][k] = dp[i][k]
        if row[k - 1] != float('inf'):
            dp[i + 1][k] = min(dp[i + 1][k], row[k - 1] + len_meeting)

best = 0
for i in range(n + 1):
    for days in range(n + 1):
        if dp[i][days] <= max_allowed:
            best = max(best, days)

print(best)