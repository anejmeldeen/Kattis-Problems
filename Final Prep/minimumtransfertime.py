from collections import defaultdict
import heapq

n, t = list(map(int, input().split()))

target_locs = set()
start_locs = set()

loc_to_id = {}
graph = defaultdict(list)
deps = defaultdict(list)
arrs = defaultdict(list)
curr_id = 1

for _ in range(t):
    u, v, dep, arr = list(map(int, input().split()))

    if (u, dep) not in loc_to_id:
        loc_to_id[(u, dep)] = curr_id
        curr_id += 1
    key1 = loc_to_id[(u, dep)]

    if (v, arr) not in loc_to_id:
        loc_to_id[(v, arr)] = curr_id
        curr_id += 1
    key2 = loc_to_id[(v, arr)]

    if u == n:
        target_locs.add(key1)
    elif v == n:
        target_locs.add(key2)
    if u == 1:
        start_locs.add((key1, dep))
    elif v == 1:
        start_locs.add((key2, arr))

    graph[key1].append((key2, 0))
    deps[u].append((key1, dep))
    arrs[v].append((key2, arr))

events = defaultdict(list)
for i in range(1, n + 1):
    for dep in deps[i]:
        events[i].append(dep)
    for arr in arrs[i]:
        events[i].append(arr)
    events[i].sort(key=lambda x: x[1])
    arr = events[i]
    for i in range(len(arr) - 1):
        curr = arr[i]
        next = arr[i + 1]
        if next[1] >= curr[1]:
            graph[curr[0]].append((next[0], next[1] - curr[1]))

for loc in start_locs:
    loc_loc, loc_time = loc
    graph[0].append((loc_loc, loc_time))

heap = [(0, 0)]
seen = set()
while heap:
    cost, loc = heapq.heappop(heap)

    if loc in seen:
        continue
    seen.add(loc)

    if loc in target_locs:
        print(cost)
        exit()

    for conn_loc, conn_cost in graph[loc]:
        if conn_loc in seen:
            continue
        heapq.heappush(heap, (cost + conn_cost, conn_loc))

print(-1)