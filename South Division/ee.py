n, m = list(map(int, input().split()))

dp = [[0] * (201) for _ in range(201)]
for j in range(201):
    dp[0][j] = 1
    dp[1][j] = j

for total in range(4, 401):
    for i in range(max(2, total - 200), min(total, 201)):
        j = total - i
        if j < 2:
            continue
        for choice in range(1, i // 2 + 1):
            dp[i][j] = max(dp[i][j], i * j - dp[j][choice] - dp[j][i - choice])

best = 0
res = -1
for choice in range(1, n // 2 + 1):
    chance = n * m - dp[m][choice] - dp[m][n - choice]
    if chance > best:
        best = chance
        res = choice

print(res)