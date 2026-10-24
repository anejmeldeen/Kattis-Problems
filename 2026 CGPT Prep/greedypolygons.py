import math

n, d, g = list(map(int, input().split()))

points = []
for _ in range(n):
    points.append(tuple(map(int, input().split())))

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(pts):
    area = 0
    for i in range(len(pts)):
        j = (i + 1) % len(pts)
        area += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
    return abs(area) / 2.0

points = convex_hull(points)
area = polygon_area(points)

gain = 0
gain_dist = g * d
for i in range(len(points)):
    j = (i + 1) % len(points)
    point_i = points[i]
    point_j = points[j]
    dist = ((point_i[0] - point_j[0]) ** 2 + (point_i[1] - point_j[1]) ** 2) ** 0.5
    gain += dist * gain_dist

def angle_between(a, b, c):
    ux, uy = a[0] - b[0], a[1] - b[1]
    vx, vy = c[0] - b[0], c[1] - b[1]
    dot = ux * vx + uy * vy
    cross = ux * vy - uy * vx
    return math.atan2(abs(cross), dot)

for i in range(len(points)):
    prev = (i - 1) % (len(points))
    next = (i + 1) % (len(points))
    angle = angle_between(points[prev], points[i], points[next])
    angle = math.pi - angle

    circle = math.pi * gain_dist ** 2
    circle *= angle / (2 * math.pi)

    gain += circle

print(area + gain)