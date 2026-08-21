import heapq

v, e = list(map(int, input().split()))
graph = {}

for _ in range(e):
    x, y, cost = list(map(int, input().split()))
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
    graph[x].append((cost, y))

s, t = list(map(int, input().split()))
heap = [(0, s, -1, 0)]
seen = set()
optimal_t_cost = -1
sol = 0
counts = {(0, s): 1}
while heap:
    data = heapq.heappop(heap)
    curr_cost, curr_loc, prev, prev_cost = data
    counts[(curr_cost, curr_loc)] = counts.get((curr_cost, curr_loc), 0) + counts.get((curr_cost - prev_cost, prev), 0)
    if curr_loc == t:
        if optimal_t_cost == -1:
            optimal_t_cost = curr_cost

    if curr_loc in seen:
        continue

    seen.add(curr_loc)
    if curr_loc in graph:
        for conn_cost, conn_loc in graph[curr_loc]:
            if conn_loc not in seen or conn_loc == t:
                heapq.heappush(heap, (curr_cost + conn_cost, conn_loc, curr_loc, conn_cost))

print(counts.get((optimal_t_cost, t), 0))