from collections import deque

while (data := input()) != "-1":
    x_max, y_max, t, l, w, = list(map(int, data.split()))
    data = []
    while len(data) < 2 * l + 4 * w:
        data += list(map(int, input().split()))

    water_pos = data[:2*l]
    walls = data[2*l:]
    seen = set()
    wall_set = set()

    for idx in range(0, 4 * w, 4):
        sx, sy, ex, ey = walls[idx], walls[idx + 1], walls[idx + 2], walls[idx + 3]
        if sy == ey:
            for x in range(min(sx, ex), max(sx, ex) + 1):
                wall_set.add((x, sy))
        elif sx == ex:
            for y in range(min(sy, ey), max(sy, ey) + 1):
                wall_set.add((sx, y))
        else:
            if sx > ex:
                sx, sy, ex, ey = ex, ey, sx, sy
            if ey > sy:
                for shift in range(ex - sx + 1):
                    wall_set.add((sx + shift, sy + shift))
            else:
                for shift in range(ex - sx + 1):
                    wall_set.add((sx + shift, sy - shift))

    queue = deque()
    for idx in range(0, 2 * l, 2):
        x, y = water_pos[idx], water_pos[idx + 1]
        if (x, y) not in wall_set:
            queue.append((x, y, 1))
            seen.add((x, y))

    while queue:
        data = queue.popleft()
        x, y, dist = data

        for direction in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if (new_x, new_y) in seen or dist == t or new_x <= 0 or new_y <= 0 or new_x > x_max or new_y > y_max or (new_x, new_y) in wall_set:
                continue
            queue.append((new_x, new_y, dist + 1))
            seen.add((new_x, new_y))

    print(len(seen))