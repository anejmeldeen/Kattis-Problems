import heapq
from collections import defaultdict

n, m, a, b = list(map(int, input().split()))

graph = defaultdict(list)

total = 0
edges = []
for _ in range(m):
    x, y, l = list(map(int, input().split()))
    total += l
    graph[x].append((y, l))
    graph[y].append((x, l))
    edges.append((x, y, l))

da = defaultdict(int)
db = defaultdict(int)

def distance_grabber(a, b):
    heap = [(0, a)]
    seen = set()
    res = float('inf')
    while heap:
        cost, loc = heapq.heappop(heap)

        if loc in seen:
            continue
        seen.add(loc)

        if loc == b:
            res = cost
            break

        for conn_loc, conn_cost in graph[loc]:
            if conn_loc not in seen:
                heapq.heappush(heap, (cost + conn_cost, conn_loc))
    return res

for i in range(1, n + 1):
    da[i] = distance_grabber(i, a)
    db[i] = distance_grabber(i, b)
res = da[b]

edge_cost = 0
for edge in edges:
    x, y, w = edge
    if (da[x] + db[y] + w) == res or (db[x] + da[y] + w) == res:
        edge_cost += w

print(total - edge_cost)