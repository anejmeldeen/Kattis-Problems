s, r, f, t = list(map(int, input().split()))

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
    
dinic = Dinic(2 + s + t * 2)
materials = set(input().split())
factories = set(input().split())
ids = {}

curr = 2
for mat in materials:
    if mat not in ids:
        ids[mat] = curr
        curr += 1
    mat_id = ids[mat]
    dinic.add_edge(0, mat_id, 1)

for fac in factories:
    if fac not in ids:
        ids[fac] = curr
        curr += 1
    fac_id = ids[fac]
    dinic.add_edge(fac_id, 1, 1)

for _ in range(t):
    data = input().split()
    num = int(data[0])
    nodes = data[1:]

    for node in nodes:
        if node not in ids:
            ids[node] = curr
            curr += 1

    mat_nodes = set()
    fac_nodes = set()
    other_nodes = set()
    for node in nodes:
        if node in materials:
            mat_nodes.add(ids[node])
        elif node in factories:
            fac_nodes.add(ids[node])
        else:
            other_nodes.add(ids[node])

    company_id = curr
    company_id2 = curr + 1
    curr += 2

    dinic.add_edge(company_id, company_id2, 1)
    for mat_node in mat_nodes:
        dinic.add_edge(mat_node, company_id, 1)
    for fac_node in fac_nodes:
        dinic.add_edge(company_id2, fac_node, 1)
    for other_node in other_nodes:
        dinic.add_edge(other_node, company_id, 1)
        dinic.add_edge(company_id2, other_node, 1)

print(dinic.max_flow(0, 1))