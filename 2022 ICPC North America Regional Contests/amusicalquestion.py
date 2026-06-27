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
bests = [0, 0]
best_diff = 0
for x in range(c + 1):
    for y in range(c + 1):
        if dp[x][y] and (x + y) > best:
            best = x + y
            bests = [max(x, y), min(x, y)]
            best_diff = abs(x - y)
        elif dp[x][y] and (x + y) == best and abs(x - y) < best_diff:
            best_diff = abs(x - y)
            bests = [max(x, y), min(x, y)]

print(bests[0], bests[1])