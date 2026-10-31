t = int(input())

def get_intersects(x1, y1, x2, y2):
    intersects = set()
    slope = (y2 - y1) / (x2 - x1)
    y_int = y1 - x1 * slope

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for x in range(min_x, max_x + 1):
        intersects.add((x, slope * x + y_int))
    for y in range(min_y, max_y + 1):
        intersects.add(((y - y_int) / slope, y))

    return list(intersects)

for _ in range(t):
    bx1, by1, bx2, by2, x1, y1, x2, y2 = list(map(int, input().split()))
    intersects = get_intersects(bx1, by1, bx2, by2)

    best = abs(x1 - x2) + abs(y1 - y2)
    for entry_loc in intersects:
        for exit_loc in intersects:
            dist = abs(entry_loc[0] - x1) + abs(entry_loc[1] - y1)
            dist += abs(exit_loc[0] - x2) + abs(exit_loc[1] - y2)
            dist += ((entry_loc[0] - exit_loc[0]) ** 2 + (entry_loc[1] - exit_loc[1]) ** 2) ** 0.5
            best = min(best, dist)

    print(best)