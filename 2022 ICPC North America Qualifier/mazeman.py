import sys
sys.setrecursionlimit(int(1e9))

n, m = list(map(int, input().split()))

board = []
for _ in range(n):
    board.append(list(input()))

starting_locations = []
for i in range(n):
    for j in range(m):
        if board[i][j] not in "X .":
            starting_locations.append((i, j))

def recurse(x, y, seen):
    if board[x][y] == "X":
        return 0
    
    count = 0
    if board[x][y] == ".":
        board[x][y] = " "
        count += 1

    seen.add((x, y))

    for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        x_shift = direction[0]
        y_shift = direction[1]
        if (x + x_shift, y + y_shift) not in seen and (x + x_shift) >= 0 and (x + x_shift) < n and (y + y_shift) >= 0 and (y + y_shift) < m and board[x + x_shift][y + y_shift] in ". ":
            count += recurse(x + x_shift, y + y_shift, seen)

    return count

num_players = 0
seen = set()
for location in starting_locations:
    x = recurse(location[0], location[1], seen)
    if x > 0:
        num_players += 1

rem_dots = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == ".":
            rem_dots += 1

print(num_players, rem_dots)