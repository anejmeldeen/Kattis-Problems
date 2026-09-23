import sys
data = sys.stdin.read().split()

data_idx = 0
while data_idx < len(data):
    n = int(data[data_idx])
    m = int(data[data_idx + 1])
    data_idx += 2
    n, m = list(map(int, data[data_idx].split()))
    data_idx += 1

    node_id = [i for i in range(n + 1)]
    next_id = n + 1

    parent = [i for i in range(n + m + 1)]
    size = [1 for _ in range(n + m + 1)]
    summ = [i for i in range(n + m + 1)]

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
            summ[b] += summ[a]

    for mm in range(m):
        query = list(map(int, data[data_idx + mm].split()))
        if query[0] == 1:
            a, b = query[1], query[2]
            union(node_id[a], node_id[b])
        elif query[0] == 2:
            a, b = query[1], query[2]
            parent_a = find(node_id[a])
            size[parent_a] -= 1
            summ[parent_a] -= a
            node_id[a] = next_id
            summ[next_id] = a
            next_id += 1
            union(node_id[a], node_id[b])
        elif query[0] == 3:
            a = query[1]
            parent_a = find(node_id[a])
            print(size[parent_a], summ[parent_a])

    data_idx += m