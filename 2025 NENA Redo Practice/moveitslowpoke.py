from collections import defaultdict
import heapq

n, m, k, d, s, t = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    a, b, l = list(map(int, input().split()))
    graph[a].append((b, l))
    graph[b].append((a, l))

bads = set()
pairs = set()
for _ in range(k):
    a, b, c = list(map(int, input().split()))
    bads.add((a, b, c))
    pairs.add((a, b))
    pairs.add((b, c))

seen = set()
heap = [(0, 0, s, -1, 0)]
while heap:
    cost, conn_cost, loc, prev, prev_cost = heapq.heappop(heap)

    if loc == t:
        print(cost)
        exit()

    if (loc, prev, conn_cost) in seen:
        continue
    seen.add((loc, prev, conn_cost))

    for new_loc, path_cost in graph[loc]:
        if new_loc == prev:
            continue

        new_conn_cost = conn_cost
        if (prev, loc, new_loc) in bads:
            if new_conn_cost == 0:
                new_conn_cost += prev_cost
            new_conn_cost += path_cost
        else:
            new_conn_cost = 0

        if (new_loc, loc, new_conn_cost) in seen or new_conn_cost > d:
            continue
        heapq.heappush(heap, (cost + path_cost, new_conn_cost, new_loc, loc, path_cost))

print("impossible")