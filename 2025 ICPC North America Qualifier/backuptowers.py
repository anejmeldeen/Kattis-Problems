from collections import deque

r, c, n = list(map(int, input().split()))
cell_locs = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    cell_locs.append((x - 1, y - 1))

grid = [[0] * c for _ in range(r)]
new_grid = [[0] * c for _ in range(r)]
sent = [[0] * c for _ in range(r)]

heap = deque()
for i in range(n):
    x, y = cell_locs[i]
    heap.append((i + 1, x, y))
    sent[x][y] = i + 1

while heap:
    curr = heap.popleft()
    origin = curr[0]
    x = curr[1]
    y = curr[2]

    if grid[x][y] == 0:
        grid[x][y] = origin
    elif new_grid[x][y] == 0:
        new_grid[x][y] = origin
    else:
        continue

    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for dir_x, dir_y in dirs:
        new_x = x + dir_x
        new_y = y + dir_y
        if new_x < 0 or new_y < 0 or new_x >= r or new_y >= c:
            continue
        if sent[new_x][new_y] == origin:
            continue

        heap.append((origin, new_x, new_y))
        sent[new_x][new_y] = origin

for row in grid:
    print(' '.join(list(map(str, row))))
for row in new_grid:
    print(' '.join(list(map(str, row))))