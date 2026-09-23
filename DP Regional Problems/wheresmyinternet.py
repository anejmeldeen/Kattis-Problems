n, m = list(map(int, input().split()))

parent = [i for i in range(n + 1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[a] = b

for _ in range(m):
    a, b = list(map(int, input().split()))
    union(a, b)

count = 0
for i in range(1, n + 1):
    if find(i) != find(1):
        print(i)
        count += 1
if count == 0:
    print("Connected")