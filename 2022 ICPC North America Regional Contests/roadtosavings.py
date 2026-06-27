import heapq

n, m, a, b = list(map(int, input().split()))

graph = {}
total_length = 0
for _ in range(m):
    x, y, l = list(map(int, input().split()))
    total_length += l

    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []

    graph[x].append((l, y))
    graph[y].append((l, x))

heap = []
heapq.heappush(heap, (0, a, set(), set()))

cost_to_b = float('inf')
paths_to_b = set()

while heap:
    data = heapq.heappop(heap)
    curr_cost = data[0]
    curr_loc = data[1]
    seen = data[2]
    seen_intersects = data[3]

    if curr_loc == b:
        if curr_cost < cost_to_b:
            cost_to_b = curr_cost
            for path in seen:
                paths_to_b.add(path)
        elif curr_cost == cost_to_b:
            for path in seen:
                paths_to_b.add(path)
        continue

    seen_intersects.add(curr_loc)

    for conn_data in graph[curr_loc]:
        if conn_data[1] in seen_intersects:
            continue
        conn_cost = conn_data[0]
        conn_loc = conn_data[1]
        new_seen = seen.copy()
        new_seen.add((min(curr_loc, conn_loc), max(curr_loc, conn_loc), conn_cost))
        heapq.heappush(heap, (curr_cost + conn_cost, conn_loc, new_seen, seen_intersects))

total_cost = 0
for x in paths_to_b:
    total_cost += x[2]
print(total_length - total_cost)