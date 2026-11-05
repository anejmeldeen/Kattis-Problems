import sys
from collections import defaultdict, deque

inputs = sys.stdin.read().split()

n, m = list(map(int, [inputs[0], inputs[1]]))

values = list(map(int, inputs[2:2 + n]))

graph = defaultdict(list)
prereq_count = defaultdict(int)

idx = 2 + n

for _ in range(m):
    a, b = list(map(int, (inputs[idx], inputs[idx + 1])))
    idx += 2
    graph[a].append(b)
    prereq_count[b] += 1

culminating = set()
queue = deque()

for i in range(1, n + 1):
    if len(graph[i]) == 0:
        culminating.add(i)
    if prereq_count[i] == 0:
        queue.append((i, set([i])))

culmin_sets = []

while queue:
    book, seen = queue.popleft()

    if book in culminating:
        culmin_sets.append(seen)
        continue

    for conn in graph[book]:
        prereq_count[conn] -= 1
        if prereq_count[conn] == 0:
            seen_copy = seen.copy()
            seen_copy.add(conn)
            queue.append((conn, seen_copy))

mini = float('inf')
for i in range(len(culmin_sets)):
    for j in range(len(culmin_sets)):
        if i == j:
            continue
        need = culmin_sets[i] | culmin_sets[j]
        cost = 0
        for item in need:
            cost += values[item - 1]
        mini = min(mini, cost)

print(mini)