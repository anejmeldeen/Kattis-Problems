p = int(input())
MOD = 1001113

for _ in range(p):
    k, n, v = list(map(int, input().split()))

    dp = [[0] * (v + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, v + 1):
            dp[i][j] = (dp[i - 1][j] * (j + 1) + dp[i - 1][j - 1] * (i - j)) % MOD

    print(k, dp[n][v])