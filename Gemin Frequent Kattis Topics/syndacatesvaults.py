import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e9))

n, m = list(map(int, input().split()))
weights = list(map(int, input().split()))

graph = defaultdict(list)
reverse_graph = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    reverse_graph[b].append(a)

stack = []
seen = set()

def recurse(node):
    if node in seen:
        return
    seen.add(node)

    for conn in graph[node]:
        recurse(conn)
    stack.append(node)

for i in range(1, n + 1):
    recurse(i)

seen = set()
components = []

def gather(node, comp):
    if node in seen:
        return []
    seen.add(node)

    comp.append(node)
    for conn in reverse_graph[node]:
        gather(conn, comp)

while stack:
    arr = []
    gather(stack.pop(), arr)
    if arr:
        components.append(arr)

new_weights = []
for comp in components:
    total = 0
    for item in comp:
        total += weights[item - 1]
    new_weights.append(total)

node_to_id = {}
for i, comp in enumerate(components):
    for ele in comp:
        node_to_id[ele] = i

super_graph = defaultdict(list)
for i in range(1, n + 1):
    for conn in graph[i]:
        if node_to_id[i] != node_to_id[conn]:
            super_graph[node_to_id[i]].append(node_to_id[conn])

not_allowed = defaultdict(bool)
for i in range(len(components)):
    for ele in super_graph[i]:
        not_allowed[ele] = True

options = []
for i in range(len(components)):
    if not not_allowed[i]:
        options.append(i)

def recurse(node):
    total = new_weights[node]
    best = 0
    for conn in super_graph[node]:
        best = max(best, recurse(conn))
    return total + best

best = 0
for opt in options:
    best = max(best, recurse(opt))

print(best)