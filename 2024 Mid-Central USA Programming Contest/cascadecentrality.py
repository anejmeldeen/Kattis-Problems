from fractions import Fraction

n = int(input())
graph = {}
degrees = {}

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

for node in range(1, n + 1):
    if node not in graph:
        graph[node] = []
    degrees[node] = len(graph[node])

def dfs(node, seen, product, first):
    seen.add(node)
    summ = 0
    if not first:
        product /= degrees[node]
    for conn in graph[node]:
        seen = seen.copy()
        if conn not in seen:
            summ += dfs(conn, seen, product, False)
    return summ + product

summ = 0 
for node in range(1, n + 1):
    summ += dfs(node, set(), Fraction(1), True)

summ /= n
print(float(summ))