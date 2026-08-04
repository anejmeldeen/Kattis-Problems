n = int(input())
dp = [0] * (n + 1)
dp[0] = 1

MOD = 10**9 + 7

for i in range(1, n + 1):
    for j in range(1, 7):
        idx = i - j
        if idx >= 0:
            dp[i] += dp[idx]
            dp[i] %= MOD

print(dp[-1] % MOD)