r, c, n = list(map(int, input().split()))
board = []

for _ in range(r):
    board.append(list(map(int, input().split())))

dp = [[[float('inf')] * (n + 1) for _ in range(c)] for _ in range(r)]

for i in range(r):
    dp[i][0][0] = board[i][0] if board[i][0] != -1 else float('inf')

pass_locs = set()
for j in range(1, c - 1):
    for i in range(1, r - 1):
        left, right = board[i][j - 1], board[i][j + 1]
        up, down = board[i - 1][j], board[i + 1][j]
        if left == -1 or right == -1 or up == -1 or down == -1:
            continue
        curr = board[i][j]
        if curr > left and curr > right and curr < up and curr < down:
            pass_locs.add((i, j))

for k in range(n + 1):
    for j in range(1, c):
        for i in range(r):
            if board[i][j] == -1:
                board[i][j] = float('inf')
            use_k = k - 1 if (i, j) in pass_locs else k
            if use_k < 0:
                continue
            choice = dp[i][j - 1][use_k]
            if i > 0:
                choice = min(choice, dp[i - 1][j - 1][use_k])
            if i < r - 1:
                choice = min(choice, dp[i + 1][j - 1][use_k])
            dp[i][j][k] = choice + board[i][j]

poss = []
for i in range(r):
    poss.append(dp[i][-1][-1])
print(min(poss) if min(poss) != float('inf') else "impossible")