from collections import deque

n = int(input())
glasses = []

seen = set()

highest = 0
idx = -1

for i in range(n):
    x, y, z, r, v = list(map(int, input().split()))
    glasses.append((x, y, z, r, v))

glasses.sort(key=lambda x: x[2], reverse=True)
x_y_rad = {}
for glass in glasses:
    x, y = glass[0], glass[1]
    if (x, y) in x_y_rad and x_y_rad[(x, y)] >= glass[-2]:
        print("Invalid")
        exit()
    x_y_rad[(x, y)] = glass[-2]

queue = deque([0])
while queue:
    idx = queue.popleft()
    if idx in seen:
        continue
    seen.add(idx)

    x, y, z, r, v = glasses[idx]
    for i in range(n):
        if i == idx or i in seen:
            continue
        x2, y2, z2, r2, v2 = glasses[i]
        if z2 >= z:
            continue
        dist = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
        if dist <= r + r2:
            queue.append(i)
            seen.add(i)

if len(seen) != n:
    print("Invalid")
    exit()

total = 0
for item in seen:
    total += glasses[item][-1]
print(total / 100)