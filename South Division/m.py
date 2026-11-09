n = int(input())

points = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    a //= 100
    b //= 100
    points.append((a, b))

quadrants = [[-1] * 1000 for _ in range(1000)]
for i, loc in enumerate(points):
    a, b = loc
    if quadrants[a][b] != -1:
        quadrants[a][b] = -2
        continue
    quadrants[a][b] = i + 1

dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(1000):
    for j in range(1000):
        if quadrants[i][j] == -1 or quadrants[i][j] == -2:
            continue
        works = True
        for xdir, ydir in dirs:
            newx = i + xdir
            newy = j + ydir
            if newx < 0 or newy < 0 or newx >= 1000 or newy >= 1000:
                continue
            if quadrants[newx][newy] != -1:
                works = False
        if works:
            print(quadrants[i][j])
            exit()