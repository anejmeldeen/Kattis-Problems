n, x = list(map(int, input().split()))
coins = list(map(int, input().split()))
coins.sort()

dp = [10**9] * (x + 1)
dp[0] = 0

for i in range(1, x + 1):
    for coin in coins:
        idx = i - coin
        if idx >= 0:
            dp[i] = min(dp[i], dp[idx] + 1)
        else:
            break

print(dp[-1] if dp[-1] != 10**9 else -1)