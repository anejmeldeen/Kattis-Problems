n, k = list(map(int, input().split()))
queries = []

for _ in range(k):
    queries.append(input().split())

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

tree = FenwickTree(n)
bit_set = set()
for q in queries:
    if q[0] == "F":
        i = int(q[1])
        if i in bit_set:
            tree.add(i, -1)
            bit_set.remove(i)
        else:
            bit_set.add(i)
            tree.add(i, 1)
    else:
        l, r = int(q[1]), int(q[2])
        print(tree.query(r) - tree.query(l - 1))