r, c, n = list(map(int, input().split()))
board = [[float('inf')] * c]

for _ in range(r):
    board.append([float('inf')] + list(map(int, input().split())))

dp = [[[float('inf')] * (n + 1) for _ in range(c + 1)] for _ in range(r + 1)]

def validate(pts):
    x, y = pts
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

for i in range(r):
    dp[i][0][0] = 0

for j in range(1, c + 1):
    for i in range(1, r + 1):
        if board[i][j] == -1:
            continue

        is_pass = False
        if i > 0 and j > 0 and i < r and j < c and board[i][j - 1] < board[i][j] and board[i][j + 1] < board[i][j] and board[i][j] < board[i + 1][j] and board[i][j] < board[i - 1][j] and board[i][j - 1] != -1 and board[i][j + 1] != -1 and board[i - 1][j] != -1 and board[i + 1][j] != -1:
            is_pass = True

        for k in range(n, -1, -1):
            real_k = k - (1 if is_pass else 0)
            if real_k == -1:
                continue
            dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][real_k] + board[i][j])
            if i > 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][real_k] + board[i][j])
            if i < r:
                dp[i][j][k] = min(dp[i][j][k], dp[i + 1][j - 1][real_k] + board[i][j])

best = float('inf')
for i in range(r + 1):
    best = min(best, dp[i][-1][n])

print(best if best != float('inf') else "impossible")