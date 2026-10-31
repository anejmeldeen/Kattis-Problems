import sys
sys.setrecursionlimit(int(1e9))

r, c = list(map(int, input().split()))
board = []

for _ in range(r):
    board.append(input())

a_loc = -1, -1
b_loc = -1, -1

for i in range(r):
    for j in range(c):
        if board[i][j] == "A":
            a_loc = i, j
        elif board[i][j] == "B":
            b_loc = i, j

seen = [[False] * c for _ in range(r)]

def dfs(x, y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return float('-inf')
    if seen[x][y] or board[x][y] != ".":
        return 0
    seen[x][y] = True
    total = 1
    total += dfs(x - 1, y)
    total += dfs(x + 1, y)
    total += dfs(x, y - 1)
    total += dfs(x, y + 1)
    return total

sols = []
for i in range(r):
    for j in range(c):
        count = dfs(i, j)
        if count > 0:
            sols.append(count)

a_locs = set()
b_locs = set()

def dfs(x, y, my_dir, setty, letter):
    global a_dir, b_dir

    if x < 0 or y < 0 or x >= r or y >= c or (x, y) in setty or board[x][y] not in [letter, "X"]:
        return
    setty.add((x, y))
    new_x = x + (1 if my_dir == 0 else 0) + (-1 if my_dir == 2 else 0)
    new_y = y + (1 if my_dir == 1 else 0) + (-1 if my_dir == 3 else 0)

    if new_x < 0 or new_y < 0 or new_x >= r or new_y >= c or board[new_x][new_y] != "X":
        dfs(x - 1, y, 2, setty, letter)
        dfs(x + 1, y, 0, setty, letter)
        dfs(x, y - 1, 3, setty, letter)
        dfs(x, y + 1, 1, setty, letter)
    else:
        dfs(new_x, new_y, my_dir, setty, letter)

for my_dir in range(4):
    dfs(a_loc[0], a_loc[1], my_dir, a_locs, "A")
    dfs(b_loc[0], b_loc[1], my_dir, b_locs, "B")

def wall_dfs(x, y, walls, seen):
    if x < 0 or y < 0 or x >= r or y >= c:
        return float('-inf')
    if (x, y) in seen:
        return 0
    seen.add((x, y))
    if (x, y) in walls:
        return 0
    total = 1 if board[x][y] == "." else 0
    total += wall_dfs(x - 1, y, walls, seen)
    total += wall_dfs(x + 1, y, walls, seen)
    total += wall_dfs(x, y - 1, walls, seen)
    total += wall_dfs(x, y + 1, walls, seen)
    return total

a_total = 0
b_total = 0
total = sum(sols)
a_seen = set()
b_seen = set()
for i in range(r):
    for j in range(c):
        a_total = max(a_total, wall_dfs(i, j, a_locs, a_seen))
        b_total = max(b_total, wall_dfs(i, j, b_locs, b_seen))

intersect = a_total + b_total - total
print(a_total - intersect, b_total - intersect, intersect)