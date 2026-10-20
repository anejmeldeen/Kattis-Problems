n, m = list(map(int, input().split()))
board = []

for _ in range(n):
    board.append(list(input()))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != "#":
        return
    board[x][y] = "."
    dfs(x - 1, y - 1)
    dfs(x, y - 1)
    dfs(x + 1, y - 1)
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x - 1, y + 1)
    dfs(x, y + 1)
    dfs(x + 1, y + 1)

count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "#":
            count += 1
            dfs(i, j)

print(count)