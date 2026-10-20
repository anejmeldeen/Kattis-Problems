from collections import deque

c, r, e = list(map(int, input().split()))

char_to_orientation = {e: i for i, e in enumerate("NESW")}

robot_data = input().split()
robot1_x, robot1_y, robot1_oreintation = int(robot_data[0]), int(robot_data[1]), char_to_orientation[robot_data[2]]
robot2_x, robot2_y, robot2_oreintation = int(robot_data[3]), int(robot_data[4]), char_to_orientation[robot_data[5]]

restrictions = set()

for i in range(1, r + 1):
    restrictions.add((1, i, 3))
    restrictions.add((c, i, 1))
for j in range(1, c + 1):
    restrictions.add((j, 1, 2))
    restrictions.add((j, r, 0))

wall_restrictions = set()
horizontal_data = list(map(int, input().split()))
idx = 1
for _ in range(horizontal_data[0]):
    ci, ri = horizontal_data[idx], horizontal_data[idx + 1]
    idx += 2
    wall_restrictions.add((ci, ri, 0))
    wall_restrictions.add((ci, ri + 1, 2))

vertical_data = list(map(int, input().split()))
idx = 1
for _ in range(vertical_data[0]):
    ci, ri = vertical_data[idx], vertical_data[idx + 1]
    idx += 2
    wall_restrictions.add((ci, ri, 1))
    wall_restrictions.add((ci + 1, ri, 3))

restrictions |= wall_restrictions

queue = deque()
queue.append((0, 0, robot1_x, robot1_y, robot2_x, robot2_y))
seen = set()

def travel(x, y, direc):
    if direc == 0:
        new_x, new_y = x, y + 1
    elif direc == 1:
        new_x, new_y = x + 1, y
    elif direc == 2:
        new_x, new_y = x, y - 1
    else:
        new_x, new_y = x - 1, y

    if y == 0:
        return (x, y, 0)
    if new_y == 0 and new_x == e:
        return (new_x, new_y, 0)
    if ((x, y, direc) not in restrictions):
        return (new_x, new_y, 0)
    return (x, y, 1)

while queue:
    moves, bumps, r1_x, r1_y, r2_x, r2_y = queue.popleft()

    if (r1_x, r1_y, r2_x, r2_y) in seen:
        continue
    seen.add((r1_x, r1_y, r2_x, r2_y))

    if r1_y == 0 and r2_y == 0:
        print(moves, bumps)
        exit()

    for dir_shift in range(4):
        r1_dir = (dir_shift + robot1_oreintation) % 4
        r2_dir = (dir_shift + robot2_oreintation) % 4

        r1_travel = travel(r1_x, r1_y, r1_dir)
        r2_travel = travel(r2_x, r2_y, r2_dir)

        new_r1_x, new_r1_y, r1_bumps = r1_travel
        new_r2_x, new_r2_y, r2_bumps = r2_travel

        if (new_r1_x, new_r1_y, new_r2_x, new_r2_y) not in seen:
            queue.append((moves + 1, bumps + r1_bumps + r2_bumps, new_r1_x, new_r1_y, new_r2_x, new_r2_y))

print("hi")