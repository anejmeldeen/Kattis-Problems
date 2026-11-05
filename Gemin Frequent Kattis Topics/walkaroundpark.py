import sys
from collections import defaultdict, deque

sys.setrecursionlimit(int(1e8))

n = int(input())
adj = []

for i in range(n):
    adj.append(list(map(int, input().split())))

adj_graph = defaultdict(list)
rev_graph = defaultdict(list)

for i in range(n):
    for j in range(n):
        if adj[i][j]:
            adj_graph[i].append(j)
            rev_graph[j].append(i)

def kosaraju(adj, rev_adj, n):
    visited = [False] * n
    order, scc = [], []
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]: dfs1(v)
        order.append(u)
    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in rev_adj[u]:
            if not visited[v]: dfs2(v, comp)
    for i in range(n):
        if not visited[i]: dfs1(i)
    visited = [False] * n
    for i in reversed(order):
        if not visited[i]:
            comp = []
            dfs2(i, comp)
            scc.append(comp)
    return scc

scc = kosaraju(adj_graph, rev_graph, n)

id_to_component = {i: e for i, e in enumerate(scc)}
component_to_id = {}
for i in range(len(scc)):
    for ele in scc[i]:
        component_to_id[ele] = i

mega_graph = defaultdict(set)
for i in range(n):
    for j in range(n):
        if adj[i][j]:
            id_i, id_j = component_to_id[i], component_to_id[j]
            if id_i != id_j:
                mega_graph[id_i].add(id_j)

queue = deque()
alive_keys = set(id_to_component.keys())
out_degree = defaultdict(int)
out_in = defaultdict(set)
for key in id_to_component:
    out_degree[key] = len(mega_graph[key])
    for item in mega_graph[key]:
        out_in[item].add(key)
    if out_degree[key] == 0:
        queue.append(key)
        alive_keys.remove(key)

count = 0
while queue:
    key = queue.pop()
    nodes = id_to_component[key]

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i == j:
                continue
            if adj[nodes[i]][nodes[j]] == 0:
                count += 1

    for aliv_key in alive_keys:
        alive_nodes = id_to_component[aliv_key]
        for node in alive_nodes:
            for to_node in nodes:
                if adj[node][to_node] == 0:
                    count += 1

    for item in out_in[key]:
        out_degree[item] -= 1
        if out_degree[item] == 0:
            queue.append(item)
            alive_keys.remove(item)
    
print(count)