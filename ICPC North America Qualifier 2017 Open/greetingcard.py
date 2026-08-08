import math

n = int(input())
points = set()

for _ in range(n):
    points.add(tuple(map(int, input().split())))

pairs = set()
for i in range(2019):
    diff = 2018 ** 2 - i ** 2
    j = int(math.sqrt(diff))
    if j ** 2 == diff:
        pairs.add((i, j))
        pairs.add((-i, j))
        pairs.add((i, -j))
        pairs.add((-i, -j))

count = 0
for x, y in points:
    for pair in pairs:
        if (x + pair[0], y + pair[1]) in points:
            count += 1

print(count // 2)