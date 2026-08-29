from collections import deque

n, m = list(map(int, input().split()))
board = []

for _ in range(n):
    board.append(input())

queue = deque()
seen = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == "-":
            queue.append((0, i, j))
            seen[i][j] = 1

for i in range(n):
    if not seen[i][0]:
        seen[i][0] = 1
        queue.append((1, i, 0))
    if not seen[i][m - 1]:
        seen[i][m - 1] = 1
        queue.append((1, i, m - 1))
for j in range(m):
    if not seen[0][j]:
        seen[0][j] = 1
        queue.append((1, 0, j))
    if not seen[n - 1][j]:
        seen[n - 1][j] = 1
        queue.append((1, n - 1, j))

maxi = -1
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
while queue:
    cost, x, y = queue.popleft()
    maxi = max(maxi, cost)

    for xdir, ydir in dirs:
        new_x = x + xdir
        new_y = y + ydir
        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or seen[new_x][new_y]:
            continue
        queue.append((cost + 1, new_x, new_y))
        seen[new_x][new_y] = 1

print(maxi)