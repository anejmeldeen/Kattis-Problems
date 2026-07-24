n, m = list(map(int, input().split()))
one_set = set([1])

graph = {}

def dfs(node):
    if node in one_set:
        return
    one_set.add(node)
    for conn in graph[node]:
        if conn not in one_set:
            dfs(conn)

pairs = []
for _ in range(m):
    pairs.append(list(map(int, input().split())))

found = False
for i in range(m):
    a, b = pairs[i]
    a, b = min(a, b), max(a, b)

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

    if a in one_set:
        dfs(b)
    elif b in one_set:
        dfs(a)

    if len(one_set) == n:
        print(i + 1)
        found = True
        break

if not found:
    if n == 1:
        print(0)
    else:
        print(-1)