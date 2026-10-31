from collections import defaultdict

n, m, s, t = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

counts = defaultdict(int)
counts[s] += 1

for _ in range(t):
    new_counts = defaultdict(int)
    for loc in counts:
        for neighbor in graph[loc]:
            new_counts[neighbor] += counts[loc]
    counts = new_counts

total = 0
for key in counts:
    total += counts[key]
print(total)