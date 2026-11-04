from collections import defaultdict, deque
import sys

inputs = sys.stdin.readlines()

n = int(inputs[0])

points = []
for line in inputs[1:]:
    points.append(list(map(int, line.split())))

row_counts = defaultdict(int)
col_counts = defaultdict(int)

rows = defaultdict(set)
cols = defaultdict(set)

for i, point in enumerate(points):
    x, y = point
    row_counts[x] += 1
    col_counts[y] += 1
    rows[x].add(i)
    cols[y].add(i)

queue = deque()
seen = set()

for i, point in enumerate(points):
    x, y = point
    if row_counts[x] == 1 or col_counts[y] == 1:
        queue.append((i, 1))
        seen.add(i)

days = [float('inf')] * n

while queue:
    i, day = queue.popleft()
    x, y = points[i]

    days[i] = day

    row_counts[x] -= 1
    col_counts[y] -= 1

    rows[x].remove(i)
    cols[y].remove(i)

    if row_counts[x] == 1:
        j = rows[x].pop()
        rows[x].add(j)
        if j not in seen:
            queue.append((j, day + 1))
            seen.add(j)

    if col_counts[y] == 1:
        j = cols[y].pop()
        cols[y].add(j)
        if j not in seen:
            queue.append((j, day + 1))
            seen.add(j)

maxi = -1
best = -1

for i, day in enumerate(days):
    if day > maxi:
        maxi = day
        best = i + 1

print(best)