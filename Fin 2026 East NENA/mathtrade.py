from collections import defaultdict

n = int(input())

graph = defaultdict(list)

items = set()

for _ in range(n):
    data = input().split()
    items.add(data[1])
    graph[data[1]].append(data[2])

def dfs(item, og, dist):
    if dist > 0 and item == og:
        return dist
    sol = -1
    for next_item in graph[item]:
        sol = dfs(next_item, og, dist + 1)
    return sol

longest = 0
for item in items:
    trial = dfs(item, item, 0)
    longest = max(longest, trial)

if longest == 0:
    print("No trades possible")
else:
    print(longest)