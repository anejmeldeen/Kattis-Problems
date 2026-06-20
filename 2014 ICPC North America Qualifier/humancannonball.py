import math
import heapq

sx, sy = list(map(float, input().split()))
ex, ey = list(map(float, input().split()))
n = int(input())

locs = [(sx, sy, False), (ex, ey, False)]
for _ in range(n):
    x, y = list(map(float, input().split()))
    locs.append((x, y, True))

graph = {i: [] for i in range(n + 2)}
for i in range(n + 2):
    for j in range(n + 2):
        if i == j:
            continue
            
        loc_i = locs[i]
        loc_j = locs[j]
        dist = math.sqrt((loc_i[0] - loc_j[0]) ** 2 + (loc_i[1] - loc_j[1]) ** 2)

        cost = dist / 5
        if loc_i[2]:
            cost = min(cost, 2 + abs(dist - 50) / 5)
        graph[i].append((cost, j))

        cost = dist / 5
        if loc_j[2]:
            cost = min(cost, 2 + abs(dist - 50) / 5)
        graph[j].append((cost, i))

heap = [(0, 0)]
sol = -1
seen = set()
while heap:
    curr_cost, curr_loc = heapq.heappop(heap)
    if curr_loc in seen:
        continue
    seen.add(curr_loc)
    if curr_loc == 1:
        sol = curr_cost
        break
    for conn in graph[curr_loc]:
        conn_cost, conn_loc = conn
        if conn_loc not in seen:
            heapq.heappush(heap, (curr_cost + conn_cost, conn_loc))

print(sol)