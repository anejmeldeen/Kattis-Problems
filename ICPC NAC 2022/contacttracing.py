n, k, c = list(map(int, input().split()))
days_to_graph = {}
people_prefix = {}

for i in range(n):
    people_prefix[i + 1] = [0] * (k + 1)

for _ in range(c):
    a, b, d = list(map(int, input().split()))
    if d not in days_to_graph:
        days_to_graph[d] = {}
    graph = days_to_graph[d]
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

    people_prefix[a][d] += 1
    people_prefix[b][d] += 1

for i in range(n):
    arr = people_prefix[i + 1]
    for j in range(1, k + 1):
        arr[j] += arr[j - 1]

sol = set()

curr_queue = set([x for x in range(1, n + 1)])
for i in range(1, k + 1):
    tomorrow = set()
    while curr_queue:
        potential = curr_queue.pop()
        arr = people_prefix[potential]
        if arr[-1] - arr[i] > 0:
            continue
        if i in days_to_graph and potential in days_to_graph[i]:
            for conn in days_to_graph[i][potential]:
                tomorrow.add(conn)
    curr_queue = tomorrow
sol = sol | curr_queue

sol = list(sol)
print(len(sol))
sol.sort()
for x in sol:
    print(x)