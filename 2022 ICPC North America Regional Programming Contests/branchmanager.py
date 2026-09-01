import sys
sys.setrecursionlimit(int(1e9))

n, m = list(map(int, input().split()))
graph = {}

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
for x in range(1, n + 1):
    graph[x].sort()

destinations = []
for _ in range(m):
    destinations.append(int(input()))

in_order = {}
out_order = {}
timer = 1
def recurse(node):
    global timer
    in_order[node] = timer
    timer += 1
    for conn in graph[node]:
        recurse(conn)
    out_order[node] = timer
    timer += 1
recurse(1)

max_in = count = 0
for d in destinations:
    if out_order[d] < max_in:
        break
    if in_order[d] > max_in:
        max_in = in_order[d]
    count += 1

print(count)