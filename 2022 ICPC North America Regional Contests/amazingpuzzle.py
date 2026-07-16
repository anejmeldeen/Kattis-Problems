from collections import deque

c, r, e = list(map(int, input().split()))
robot_data = input().split()

char_to_num = {e: i for i, e in enumerate("NESW")}
diff = (char_to_num[robot_data[5]] - char_to_num[robot_data[2]]) % 4

graph = {}
for col in range(1, c + 1):
    for row in range(1, r + 1):
        conns = set()
        if col > 1:
           conns.add((col - 1, row))
        if row > 1:
            conns.add((col, row - 1))
        if col < c:
            conns.add((col + 1, row))
        if row < r:
            conns.add((col, row + 1))
        graph[(col, row)] = conns
graph[(e, 1)].add((e, 0))
graph[(e, 0)] = set()

horizontal_walls = list(map(int, input().split()))
idx = 1
for _ in range(horizontal_walls[0]):
    col, row = horizontal_walls[idx], horizontal_walls[idx + 1]
    graph[(col, row)].discard((col, row + 1))
    graph[(col, row + 1)].discard((col, row))
    idx += 2

vertical_walls = list(map(int, input().split()))
idx = 1
for _ in range(vertical_walls[0]):
    col, row = vertical_walls[idx], vertical_walls[idx + 1]
    graph[(col, row)].discard((col + 1, row))
    graph[(col + 1, row)].discard((col, row))
    idx += 2

def dir_shift(col, row, dir_num):
    ncol, nrow = col, row
    if dir_num == 0:
        nrow += 1
    elif dir_num == 1:
        ncol += 1
    elif dir_num == 2:
        nrow -= 1
    elif dir_num == 3:
        ncol -= 1
    return ncol, nrow 

queue = deque()
queue.append((0, 0, int(robot_data[0]), int(robot_data[1]), int(robot_data[3]), int(robot_data[4])))
seen = [[[[False] * (r + 1) for _ in range(c + 1)] for _ in range(r + 1)] for _ in range(c + 1)]
seen[int(robot_data[0])][int(robot_data[1])][int(robot_data[3])][int(robot_data[4])] = True
sol = (-1, -1)
while queue:
    data = queue.popleft()
    forwards, bumps, col1, row1, col2, row2 = data

    if col1 == e and row1 == 0 and col2 == e and row2 == 0:
        sol = (forwards, bumps)
        break

    for dir_num in range(4):
        ncol1, nrow1 = dir_shift(col1, row1, dir_num)
        ncol2, nrow2 = dir_shift(col2, row2, (dir_num + diff) % 4)
        new_bumps = 0
        
        if (ncol1, nrow1) not in graph[(col1, row1)]:
            ncol1, nrow1 = col1, row1
            if (ncol1 != e or nrow1 != 0):
                new_bumps += 1

        if (ncol2, nrow2) not in graph[(col2, row2)]:
            ncol2, nrow2 = col2, row2
            if (ncol2 != e or nrow2 != 0):
                new_bumps += 1

        if not seen[ncol1][nrow1][ncol2][nrow2]:
            if (ncol1 != e or nrow1 != 0) and ncol1 == ncol2 and nrow1 == nrow2:
                continue
            seen[ncol1][nrow1][ncol2][nrow2] = True
            queue.append((forwards + 1, bumps + new_bumps, ncol1, nrow1, ncol2, nrow2))
        
print(sol[0], sol[1])