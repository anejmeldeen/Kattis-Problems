t = int(input())
for _ in range(t):
    m = int(input())
    
    parent = {}
    size = {}

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[a] = b
            size[b] += size[a]
        print(size[b])

    for _ in range(m):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
        union(a, b)