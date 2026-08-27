import math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False

n, e, p = list(map(int, input().split()))
solver = DSU(n)
for i in range(2, e + 1):
    solver.union(0, i - 1)

locations = []
for _ in range(n):
    locations.append(list(map(float, input().split())))
for _ in range(p):
    a, b = list(map(int, input().split()))
    solver.union(a - 1, b - 1)

all_pairs = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            x1, y1 = locations[i - 1]
            x2, y2 = locations[j - 1]
            cost = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            all_pairs.append((cost, (i - 1, j - 1)))

all_pairs.sort()

total = 0
for cost, pair in all_pairs:
    if solver.union(*pair):
        total += cost

print(total)