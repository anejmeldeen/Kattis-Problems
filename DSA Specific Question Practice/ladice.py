import sys
sys.setrecursionlimit(int(1e9))

n, l = list(map(int, input().split()))
locations = []

for _ in range(n):
    locations.append(list(map(int, input().split())))

parent = [i for i in range(l + 1)]
size = [1] * (l + 1)
items = [0] * (l + 1)

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
        items[b] += items[a]
    items[b] += 1
    if items[b] > size[b]:
        items[b] -= 1
        return False
    return True

for a, b in locations:
    if union(a, b):
        print("LADICA")
    else:
        print("SMECE")