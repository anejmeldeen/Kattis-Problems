n, m = list(map(int, input().split()))

owed = []
for _ in range(n):
    owed.append(int(input()))

parent = [i for i in range(n)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b

for _ in range(m):
    a, b = list(map(int, input().split()))
    union(a, b)

mappy = {}
for i in range(n):
    key = find(i)
    mappy[key] = mappy.get(key, 0) + owed[i]

works = True
for key in mappy:
    if mappy[key] != 0:
        works = False
        break

print("POSSIBLE" if works else "IMPOSSIBLE")