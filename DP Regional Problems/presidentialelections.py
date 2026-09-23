import math

s = int(input())
states = []
total_votes = 0
for _ in range(s):
    d, c, f, u = list(map(int, input().split()))

    need = math.ceil((f + u - c + 1) / 2)
    if need > u:
        need = float('inf')
    need = max(0, need)

    states.append((d, need))
    total_votes += d

need = math.ceil((total_votes + 1) / 2)
dp = [float('inf')] * 3000
dp[0] = 0

for delegate_count, cost in states:
    for i in range(2999, -1, -1):
        if dp[i] != float('inf') and i + delegate_count < 3000:
            dp[i + delegate_count] = min(dp[i + delegate_count], dp[i] + cost)

best = float('inf')
for i in range(need, 3000):
    best = min(best, dp[i])

if best == float('inf'):
    print("impossible")
else:
    print(best)