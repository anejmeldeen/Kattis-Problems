from collections import deque

c, r, e = list(map(int, input().split()))
robot_data = input().split()

char_to_or = {e: i for i, e in enumerate("NESW")}

r1_x, r1_y, r1_or = int(robot_data[0]), int(robot_data[1]), char_to_or[robot_data[2]]
r2_x, r2_y, r2_or = int(robot_data[3]), int(robot_data[4]), char_to_or[robot_data[5]]

cant_go = set()

horizontal_walls = list(map(int, input().split()))
for i in range(1, horizontal_walls[0] * 2 + 1, 2):
    ci, ri = horizontal_walls[i], horizontal_walls[i + 1]
    cant_go.add((ci, ri, 0))
    cant_go.add((ci, ri + 1, 2))

vertical_walls = list(map(int, input().split()))
for i in range(1, vertical_walls[0] * 2 + 1, 2):
    ci, ri = vertical_walls[i], vertical_walls[i + 1]
    cant_go.add((ci, ri, 1))
    cant_go.add((ci + 1, ri, 3))

next_loc = [[[0] * 4 for _ in range(r + 1)] for _ in range(c + 1)]

for i in range(1, c + 1):
    for j in range(r + 1):
        for k in range(4):
            if j == 0:
                next_loc[i][j][k] = (i, j, 0)
            elif (i, j, k) in cant_go:
                next_loc[i][j][k] = (i, j, 1)
            else:
                if k == 0:
                    new_i, new_j = i, j + 1
                elif k == 1:
                    new_i, new_j = i + 1, j
                elif k == 2:
                    new_i, new_j = i, j - 1
                else:
                    new_i, new_j = i - 1, j

                if new_i == e and new_j == 0:
                    next_loc[i][j][k] = (new_i, new_j, 0)
                elif new_i <= 0 or new_j <= 0 or new_i > c or new_j > r:
                    next_loc[i][j][k] = (i, j, 1)
                else:
                    next_loc[i][j][k] = (new_i, new_j, 0)

queue = deque()
queue.append((0, r1_x, r1_y, r2_x, r2_y))
seen = [[[[False] * (r + 1) for _ in range(c + 1)] for _ in range(r + 1)] for _ in range(c + 1)]
min_bumps = [[[[float('inf')] * (r + 1) for _ in range(c + 1)] for _ in range(r + 1)] for _ in range(c + 1)]
min_bumps[r1_x][r1_y][r2_x][r2_y] = 0

while queue:
    cost, r1_x, r1_y, r2_x, r2_y = queue.popleft()
    bumps = min_bumps[r1_x][r1_y][r2_x][r2_y]

    seen[r1_x][r1_y][r2_x][r2_y] = True

    if r1_x == e and r2_x == e and r1_y == 0 and r2_y == 0:
        print(cost, bumps)
        exit()

    for orient in range(4):
        new_r1_x, new_r1_y, r1_bump = next_loc[r1_x][r1_y][(orient + r1_or) % 4]
        new_r2_x, new_r2_y, r2_bump = next_loc[r2_x][r2_y][(orient + r2_or) % 4]

        if new_r1_x == new_r2_x and new_r1_y == new_r2_y and new_r2_y != 0:
            continue
        if new_r1_x == r2_x and new_r1_y == r2_y and new_r2_x == r1_x and new_r2_y == r1_y:
            continue
        
        if not seen[new_r1_x][new_r1_y][new_r2_x][new_r2_y]:
            queue.append((cost + 1, new_r1_x, new_r1_y, new_r2_x, new_r2_y))
            seen[new_r1_x][new_r1_y][new_r2_x][new_r2_y] = True

        min_bumps[new_r1_x][new_r1_y][new_r2_x][new_r2_y] = min(min_bumps[new_r1_x][new_r1_y][new_r2_x][new_r2_y], bumps + r1_bump + r2_bump)