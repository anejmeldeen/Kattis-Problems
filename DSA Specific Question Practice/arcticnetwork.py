import math

n = int(input())

for _ in range(n):
    s, p = list(map(int, input().split()))

    outposts = []
    for _ in range(p):
        x, y = list(map(int, input().split()))
        outposts.append((x, y))

    unique = p
    parent = [i for i in range(p)]

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        global unique
        a = find(a)
        b = find(b)
        if a != b:
            parent[a] = b
            unique -= 1

    edges = []
    for i in range(p):
        for j in range(i + 1, p):
            loc_i = outposts[i]
            loc_j = outposts[j]
            cost = math.sqrt((loc_i[0] - loc_j[0]) ** 2 + (loc_i[1] - loc_j[1]) ** 2)
            edges.append((cost, i, j))
    edges.sort()

    curr = 0
    for i in range(len(edges)):
        if unique <= s:
            break
        edge = edges[i]
        curr = edge[0]
        union(edge[1], edge[2])

    print(f"{curr:.2f}")