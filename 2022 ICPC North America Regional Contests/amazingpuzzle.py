from collections import defaultdict

c, r, e = list(map(int, input().split()))

char_to_orientation = {e: i for i, e in enumerate("NESW")}

robot_data = input().split()
robot1_x, robot1_y, robot1_oreintation = int(robot_data[0]) - 1, int(robot_data[1]) - 1, char_to_orientation[robot_data[2]]
robo21_x, robot2_y, robot2_oreintation = int(robot_data[3]) - 1, int(robot_data[4]) - 1, char_to_orientation[robot_data[5]]

restrictions = set()

for i in range(r):
    restrictions.add((i, 0, 3))
    restrictions.add((i, c - 1, 1))
for j in range(c):
    restrictions.add((0, j, 0))
    restrictions.add((r - 1, j, 2))

horizontal_data = list(map(int, input().split()))
idx = 1
for _ in range(horizontal_data[0]):
    ci, ri = horizontal_data[idx], horizontal_data[idx + 1]
    idx += 2
    restrictions.add((ci, ri, 0))
    restrictions.add((ci, ri - 1, 2))

vertical_data = list(map(int, input().split()))
idx = 1
for _ in range(vertical_data[0]):
    ci, ri = vertical_data[idx], vertical_data[idx + 1]
    idx += 2
    restrictions.add((ci, ri, 3))
    restrictions.add((ci - 1, ri, 1))