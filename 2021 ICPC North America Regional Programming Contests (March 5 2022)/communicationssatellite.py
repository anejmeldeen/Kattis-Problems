import math

n = int(input())
sats = []

for _ in range(n):
    x, y, r = list(map(int, input().split()))
    sats.append((x, y, r))

conns = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        dist = math.sqrt((sats[i][0] - sats[j][0]) ** 2 + (sats[i][1] - sats[j][1]) ** 2)
        dist -= sats[i][2]
        dist -= sats[j][2]
        cost = max(dist, 0)
        conns[i].append((cost, j))
        conns[j].append((cost, i))

total = 0
seen = [False] * n
min_cost = [float('inf')] * n
min_cost[0] = 0

for _ in range(n):
    best = -1
    curr = float('inf')
    for i in range(n):
        if not seen[i] and min_cost[i] < curr:
            curr = min_cost[i]
            best = i

    i = best
    seen[i] = True
    total += min_cost[i]

    for conn in conns[i]:
        cost, j = conn
        min_cost[j] = min(min_cost[j], cost)

print(total)