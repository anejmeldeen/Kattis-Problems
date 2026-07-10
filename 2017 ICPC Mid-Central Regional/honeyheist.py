from collections import deque

r, n, a, b, x = list(map(int, input().split()))
dont_add = set(map(int, input().split()))

honey = []
for i in range(r):
    honey.append([0] * (r + i))
for i in range(r - 2, -1, -1):
    honey.append([0] * (i + r))

curr = 1
for row in honey:
    for i in range(len(row)):
        row[i] = curr
        curr += 1

graph = {}
for i in range(2 * r - 1):
    for j in range(len(honey[i])):
        graph[honey[i][j]] = []

        if i < r - 1:
            locs = [(i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
        elif i == r - 1:
            locs = [(i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j)]
        else:
            locs = [(i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j)]

        for loc in locs:
            x, y = loc
            if x >= 0 and x < 2 * r - 1:
                if y >= 0 and y < len(honey[x]):
                    if honey[x][y] not in dont_add:
                        graph[honey[i][j]].append(honey[x][y])

queue = deque()
queue.append((a, 0))
best = -1
seen = set([a])
while queue:
    curr = queue.popleft()
    curr_node = curr[0]
    curr_cost = curr[1]

    if curr_node == b:
        best = curr_cost
        break
    
    if curr_cost == n:
        continue

    for connection in graph[curr_node]:
        if connection in seen:
            continue
        queue.append((connection, curr_cost + 1))
        seen.add(connection)

if best > -1:
    print(best)
else:
    print("No")