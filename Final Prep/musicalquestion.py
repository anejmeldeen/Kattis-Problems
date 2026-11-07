c, n = list(map(int, input().split()))
arr = list(map(int, input().split()))

dp = [[False] * (c + 1) for _ in range(c + 1)]
dp[0][0] = True

for ele in arr:
    for x in range(c, -1, -1):
        for y in range(c, -1, -1):
            if dp[x][y]:
                if x + ele <= c:
                    dp[x + ele][y] = True
                if y + ele <= c:
                    dp[x][y + ele] = True

best = 0
sol = [0, 0]
for i in range(c + 1):
    for j in range(c + 1):
        if dp[i][j]:
            if i + j > best:
                best = i + j
                sol = [i, j]
            elif i + j == best:
                if abs(i - j) < abs(sol[0] - sol[1]):
                    sol = [i, j]

sol.sort(reverse=True)
print(' '.join(list(map(str, sol))))