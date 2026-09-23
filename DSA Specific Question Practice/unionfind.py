import sys
data = sys.stdin.readlines()

n, q = list(map(int, data[0].split()))

parent = [i for i in range(n)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[a] = b

outputs = []
for idx in range(q):
    curr = data[idx + 1].split()
    if curr[0] == "?":
        if find(int(curr[1])) == find(int(curr[2])):
            outputs.append("yes")
        else:
            outputs.append("no")
    else:
        union(int(curr[1]), int(curr[2]))

print('\n'.join(outputs))