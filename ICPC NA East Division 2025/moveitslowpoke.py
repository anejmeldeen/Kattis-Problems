import heapq

n, m, k, d, s, t = list(map(int, input().split()))
graph = {}

for _ in range(m):
    a, b, l = list(map(int, input().split()))
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append((l, b))
    graph[b].append((l, a))

connected_set = set()
for _ in range(k):
    a, b, c = list(map(int, input().split()))
    connected_set.add((a, b, c))

seen = set()
heap = [(0, s, 0, -1, 0)]
sol = -1
while heap:
    data = heapq.heappop(heap)
    curr_node = data[1]
    curr_cost = data[0]
    curr_conn_cost = data[2]
    prev_node = data[3]
    prev_add_cost = data[4]

    if curr_node == t:
        sol = curr_cost
        break

    seen.add((prev_node, curr_node, curr_conn_cost))

    for path_data in graph[curr_node]:
        new_node = path_data[1]
        add_cost = path_data[0]

        new_conn_cost = curr_conn_cost
        if (prev_node, curr_node, new_node) in connected_set:
            if curr_conn_cost == 0:
                new_conn_cost += prev_add_cost
            new_conn_cost += add_cost
        else:
            new_conn_cost = 0
        
        if (curr_node, new_node, new_conn_cost) in seen or new_conn_cost > d or new_node == prev_node:
            continue

        heapq.heappush(heap, (curr_cost + add_cost, new_node, new_conn_cost, curr_node, add_cost))

if sol == -1:
    print("impossible")
else:
    print(sol)