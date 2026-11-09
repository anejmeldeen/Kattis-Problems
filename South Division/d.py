d, t, w, n = list(map(int, input().split()))
need_b = t
need_a = d - t
plans = []

for _ in range(n):
    p, a, b = list(map(int, input().split()))
    plans.append((p, a, b))

plans.sort(key=lambda x:x[2], reverse=True)

dp = [[float('inf')] * (d + 1) for _ in range(d + 1)]
dp[0][min(w, d)] = 0

best = float('inf')
for i in range(n):
    new_dp = [row.copy() for row in dp]
    p, add_a, add_b = plans[i]
    for a in range(d + 1):
        for b in range(1, d + 1):
            new_a = a + add_a
            new_b = b + add_b - 1
            if new_a >= 0 and new_b >= 0:
                new_a = min(new_a, d)
                new_b = min(new_b, d)
                new_dp[new_a][new_b] = min(new_dp[new_a][new_b], dp[a][b] + p)
                if new_b >= need_b and new_b - need_b + new_a >= need_a:
                    best = min(best, new_dp[new_a][new_b])
    dp = new_dp

for a in range(d + 1):
    for b in range(d + 1):
        if b >= need_b and b - need_b + a >= need_a:
            best = min(best, dp[a][b])

print(best if best != float('inf') else -1)