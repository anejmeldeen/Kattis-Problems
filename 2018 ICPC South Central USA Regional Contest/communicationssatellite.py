n = int(input())
antennas = []
for i in range(n):
    x, y, r = list(map(int, input().split()))
    antennas.append((i, x, y, r))

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

dsu_obj = DSU(n)
seen = [False] * n
min_cost = [float('inf')] * n
min_cost[0] = 0
total = 0

for _ in range(n):
    node = -1
    best = float('inf')
    for i in range(n):
        if min_cost[i] < best and not seen[i]:
            best = min_cost[i]
            node = i
    seen[node] = True
    total += best
    for j in range(n):
        dist = ((antennas[node][1] - antennas[j][1]) ** 2 + (antennas[node][2] - antennas[j][2]) ** 2) ** 0.5
        dist -= antennas[node][3] + antennas[j][3]
        min_cost[j] = min(min_cost[j], dist)

print(total)