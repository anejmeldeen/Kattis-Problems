import math

n = int(input())

pts = []
for _ in range(n):
    x, y = list(map(float, input().split()))
    pts.append((x, y))

def dist_to_line(p, a, b):
    cross_prod = abs((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]))
    base_len = math.hypot(b[0] - a[0], b[1] - a[1])
    return cross_prod / base_len if base_len > 0 else 0

def min_polygon_width(convex_hull_points):
    n = len(convex_hull_points)
    min_width = float('inf')
    for i in range(n):
        a = convex_hull_points[i]
        b = convex_hull_points[(i + 1) % n]
        max_dist = 0
        for j in range(n):
            max_dist = max(max_dist, dist_to_line(convex_hull_points[j], a, b))
        min_width = min(min_width, max_dist)
    return min_width

print(min_polygon_width(pts))