import heapq

n = int(input())
items = list(map(int, input().split()))
m = int(input())
graph = {}

for _ in range(m):
    x, y, cost = list(map(int, input().split()))

    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []

    graph[x].append((cost, y))
    graph[y].append((cost, x))

heap = [(0, -items[0], 1)]
target = n
found = False
seen = set()
while heap:
    data = heapq.heappop(heap)
    cost, summ, loc = data

    if loc in seen:
        continue
    seen.add(loc)

    if loc == target:
        print(cost, -summ)
        found = True
        break

    if loc not in graph:
        continue
    for conn in graph[loc]:
        conn_cost, conn_loc = conn
        if conn_loc in seen:
            continue
        heapq.heappush(heap, (cost + conn_cost, summ - items[conn_loc - 1], conn_loc))

if not found:
    print("impossible")