from collections import deque

r, c, k = list(map(int, input().split()))

debris_locs = []
for _ in range(k):
    debris_locs.append(list(map(int, input().split())))

class Dinics:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, 0, len(self.graph[v])])
        self.graph[v].append([u, 0, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, flow, rev_idx in self.graph[u]:
                if cap > flow and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, push, ptr):
        if push == 0 or u == t:
            return push
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, flow, rev_idx = self.graph[u][i]
            if self.level[u] + 1 != self.level[v] or cap == flow:
                continue
            pushed = self.dfs(v, t, min(push, cap - flow), ptr)
            if pushed == 0:
                continue
            self.graph[u][i][2] += pushed
            self.graph[v][rev_idx][2] -= pushed
            return pushed
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if not pushed: break
                flow += pushed
        return flow

dinic = Dinics(2 + r + c)
for i in range(2, r + 2):
    dinic.add_edge(0, i, 1)
for j in range(r + 2, r + c + 2):
    dinic.add_edge(j, 1, 1)

for point in debris_locs:
    dinic.add_edge(point[0] + 1, point[1] + 1 + r, 1)

print(dinic.max_flow(0, 1))