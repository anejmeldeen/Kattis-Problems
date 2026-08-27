import math
x, y, x1, y1, x2, y2 = list(map(int, input().split()))
best = float('inf')

locs = []
locs.append((x1, y1))
locs.append((x2, y2))
locs.append((x1, y2))
locs.append((x2, y1))

if x1 <= x <= x2:
    locs.append((x, y1))
    locs.append((x, y2))
if y1 <= y <= y2:
    locs.append((x1, y))
    locs.append((x2, y))

for a, b in locs:
    best = min(best, math.sqrt((x - a) ** 2 + (y - b) ** 2))

print(best)