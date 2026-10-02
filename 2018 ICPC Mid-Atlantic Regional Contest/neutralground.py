from collections import deque

h, w = list(map(int, input().split()))
board = []
MAX_VAL = 1000000

for _ in range(w):
    board.append(input())

class Dinic():
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

dinic = Dinic(2 + w * h * 2)
for i in range(w):
    for j in range(h):
        id_in = (i * h + j) * 2 + 2
        id_out = id_in + 1
        if board[i][j] == "A":
            dinic.add_edge(0, id_in, MAX_VAL)
            dinic.add_edge(id_in, id_out, MAX_VAL)
        elif board[i][j] == "B":
            dinic.add_edge(id_out, 1, MAX_VAL)
            dinic.add_edge(id_in, id_out, MAX_VAL)
        else:
            dinic.add_edge(id_in, id_out, int(board[i][j]))

        for xdir, ydir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_i = i + xdir
            new_j = j + ydir
            if new_i < 0 or new_j < 0 or new_i >= w or new_j >= h:
                continue
            new_id_in = (new_i * h + new_j) * 2 + 2
            new_id_out = new_id_in + 1
            dinic.add_edge(id_out, new_id_in, MAX_VAL)
print(dinic.max_flow(0, 1))
