dp = [0] * 51
dp[0] = 1

for i in range(1, 51):
    dp[i] += dp[i - 1]
    if i >= 2:
        dp[i] += dp[i - 2]
    if i >= 3:
        dp[i] += dp[i - 3]
    if i >= 4:
        dp[i] += dp[i - 4]

print(dp[-1])