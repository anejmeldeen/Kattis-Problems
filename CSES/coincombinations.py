n, x = list(map(int, input().split()))
coins = list(map(int, input().split()))
coins.sort()

MOD = 10**9 + 7
dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x + 1):
    for coin in coins:
        idx = i - coin
        if idx >= 0:
            dp[i] += dp[idx]
            dp[i] %= MOD
        else:
            break

print(dp[-1])