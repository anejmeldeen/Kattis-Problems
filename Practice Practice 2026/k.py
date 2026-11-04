from collections import defaultdict
import heapq

n, t = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(t):
    u, v, dep, arr = list(map(int, input().split()))
    graph[u].append((v, dep, arr))

heap = [(0, 1, 0)]
seen = set()

while heap:
    cost, loc, arr = heapq.heappop(heap)

    if loc == n:
        print(cost)
        exit()
    if (loc, arr) in seen:
        continue
    seen.add((loc, arr))

    for conn_loc, dep, new_arr in graph[loc]:
        if dep < arr or (conn_loc, new_arr) in seen:
            continue
        heapq.heappush(heap, (cost + dep - arr, conn_loc, new_arr))

print(-1)