import sys
import math
from collections import deque
sys.setrecursionlimit(int(1e8))
data = sys.stdin.readlines()

class TreeLCA:
    def __init__(self, n, graph, root=1):
        self.LOG = math.ceil(math.log2(n)) + 1 if n > 1 else 1
        self.up = [[0] * self.LOG for _ in range(n + 1)]
        self.depth = [0] * (n + 1)
        
        q = deque([root])
        self.up[root][0] = 0
        self.depth[root] = 0
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v != self.up[u][0]:
                    self.up[v][0] = u
                    self.depth[v] = self.depth[u] + 1
                    q.append(v)
                    
        for j in range(1, self.LOG):
            for i in range(1, n + 1):
                self.up[i][j] = self.up[ self.up[i][j-1] ][j-1]

    def get_lca(self, u, v):
        if self.depth[u] < self.depth[v]: 
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        
        for j in range(self.LOG):
            if (diff >> j) & 1: 
                u = self.up[u][j]
                
        if u == v: 
            return u
            
        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]
                
        return self.up[u][0]

    def get_dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.get_lca(u, v)]

t = int(data[0])
idx = 1
for _ in range(t):
    n = int(data[idx])
    idx += 1
    graph = {}
    for _ in range(n - 1):
        a, b = list(map(int, data[idx].split()))
        idx += 1
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    perm = []
    for _ in range(n):
        perm.append(int(data[idx]))
        idx += 1

    lca_grabber = TreeLCA(n, graph)
    works = True
    for i in range(1, n):
        works = works and (lca_grabber.get_dist(perm[i], perm[i - 1]) <= 3)
        if not works:
            break

    if works:
        print(1)
    else:
        print(0)