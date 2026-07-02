from collections import deque

class Dinic:
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

n, m = list(map(int, input().split()))
inputs = []
total_disks = 0
for _ in range(m):
    inputs.append(list(map(int, input().split())))
    total_disks += inputs[-1][2]

low = 0
high = int(total_disks // n)
best = -1
while low <= high:
    med = (low + high) // 2
    din = Dinic(n + m + 3)
    S = n + m + 1
    T = n + m + 2
    for i in range(1, n + 1):
        din.add_edge(i, T, med)
    idx = n + 1
    for x, y, cap in inputs:
        din.add_edge(S, idx, cap)
        din.add_edge(idx, x, cap)
        din.add_edge(idx, y, cap)
        idx += 1
    flow = din.max_flow(S, T)

    if flow // n == med:
        best = med
        low = med + 1
    else:
        high = med - 1

print(total_disks - best * n)