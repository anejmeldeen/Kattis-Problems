from collections import deque

s, f, r, t = list(map(int, input().split()))

materials = set(input().split())
factories = set(input().split())
name_to_id = {}

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
        return self.level[t] > 0

    def dfs(self, u, t, push, ptr):
        if push == 0 or u == t: return push
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, flow, rev_idx = self.graph[u][i]
            if self.level[u] + 1 != self.level[v] or cap == flow: continue
            pushed = self.dfs(v, t, min(push, cap - flow), ptr)
            if pushed == 0: continue
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

curr_id = 2
dinic = Dinic(s + t * 2 + 2)
for name in materials:
    name_to_id[name] = curr_id
    curr_id += 1
    dinic.add_edge(0, name_to_id[name], 1)

for name in factories:
    name_to_id[name] = curr_id
    curr_id += 1
    dinic.add_edge(name_to_id[name], 1, 1)

for i in range(t):
    data = input().split()
    dinic.add_edge(2 + s + i, 2 + s + i + t, 1)
    for name in data[1:]:
        if name not in name_to_id:
            name_to_id[name] = curr_id
            curr_id += 1
        if name in materials:
            dinic.add_edge(name_to_id[name], 2 + s + i, 1)
        elif name in factories:
            dinic.add_edge(2 + s + i + t, name_to_id[name], 1)
        else:
            dinic.add_edge(name_to_id[name], 2 + s + i, 1)
            dinic.add_edge(2 + s + i + t, name_to_id[name], 1)

print(dinic.max_flow(0, 1))