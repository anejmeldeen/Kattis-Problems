from collections import defaultdict, deque
import heapq

n, m, k = list(map(int, input().split()))

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
    
transfers = []
for _ in range(m):
    from_loc, to_loc, time = input().split()
    from_loc, to_loc = int(from_loc), int(to_loc)
    int_time = 0

    time = time.split(":")
    int_time = int(time[0]) * 60 + int(time[1])

    transfers.append((from_loc, to_loc, int_time))

dinic = Dinic(2 + 2 * m)

distances = [[float('inf')] * (n + 1) for _ in range(n + 1)]
graph = defaultdict(list)

def get_dists(og_loc):
    seen = set()
    heap = [(0, og_loc)]
    while heap:
        cost, loc = heapq.heappop(heap)
        if loc in seen:
            continue
        seen.add(loc)
        distances[og_loc][loc] = cost
        for conn_loc, conn_cost in graph[loc]:
            if conn_loc not in seen:
                heapq.heappush(heap, (conn_cost + cost, conn_loc))

for _ in range(k):
    a, b, t1, t2 = list(map(int, input().split()))
    graph[a].append((b, t1))
    graph[b].append((a, t2))

for loc in range(1, n + 1):
    get_dists(loc)
    
for i in range(m):
    for j in range(m):
        if i == j:
            continue
        transfer_i = transfers[i]
        transfer_j = transfers[j]
        if transfer_i[2] + 60 + distances[transfer_i[0]][transfer_i[1]] + distances[transfer_i[1]][transfer_j[0]] <= transfer_j[2]:
            dinic.add_edge(i + 2, j + 2 + m, 1)

for i in range(m):
    dinic.add_edge(0, i + 2, 1)
    dinic.add_edge(i + 2 + m, 1, 1)

print(m - dinic.max_flow(0, 1))