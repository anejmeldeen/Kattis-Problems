import heapq
from collections import defaultdict

n, m, k, d, s, t = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(m):
    a, b, l = list(map(int, input().split()))
    graph[a].append((b, l))
    graph[b].append((a, l))

bad = set()
for _ in range(k):
    a, b, c = list(map(int, input().split()))
    bad.add((a, b, c))

seen = set()
heap = [(0, 0, s, -1, 0)]
while heap:
    cost, conn_cost, curr_loc, prev_loc, prev_cost = heapq.heappop(heap)

    if curr_loc == t:
        print(cost)
        exit()

    if (curr_loc, conn_cost, prev_loc) in seen:
        continue
    seen.add((curr_loc, conn_cost, prev_loc))

    for conn_loc, add_conn_cost in graph[curr_loc]:
        if conn_loc == prev_loc:
            continue
        direc = (prev_loc, curr_loc, conn_loc)
        new_conn_cost = conn_cost
        if direc in bad:
            if new_conn_cost == 0:
                new_conn_cost += prev_cost
            new_conn_cost += add_conn_cost
        else:
            new_conn_cost = 0
        new = (cost + add_conn_cost, new_conn_cost, conn_loc, curr_loc)
        if new not in seen and new_conn_cost <= d:
            heapq.heappush(heap, (cost + add_conn_cost, new_conn_cost, conn_loc, curr_loc, add_conn_cost))

print("impossible")