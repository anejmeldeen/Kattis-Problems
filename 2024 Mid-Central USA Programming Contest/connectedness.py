import sys
input_data = list(map(int, sys.stdin.read().split()))

n, m = input_data[0], input_data[1]

parent = list(range(n + 1))
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]
def union(i, j):
    root_i, root_j = find(i), find(j)
    if root_i != root_j: 
        parent[root_i] = root_j
        return True
    return False

idx = 2
num_components = n
sol = 0
for i in range(m):
    a, b = input_data[idx], input_data[idx + 1]
    idx += 2

    if union(a, b):
        num_components -= 1

    if num_components == 1:
        sol = i + 1
        break

if num_components != 1:
    print(-1)
else:
    print(sol)