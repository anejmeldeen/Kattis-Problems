import sys
sys.setrecursionlimit(int(1e9))

n, k = list(map(int, input().split()))
graph = {}

summ = 0
for _ in range(n - 1):
    a, b, c = list(map(int, input().split()))
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b, c))
    graph[b].append((a, c))
    summ += c

if k >= 2:
    print(summ)
else:
    farthest = -1
    most = 0

    def dfs(root, curr, prev):
        global farthest, most
        if curr > most:
            most = curr
            farthest = root
        for conn in graph[root]:
            if conn[0] == prev:
                continue
            dfs(conn[0], curr + conn[1], root)

    dfs(1, 0, -1)
    a = farthest
    dfs(a, 0, -1)
    print(most)