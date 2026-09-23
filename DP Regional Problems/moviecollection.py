t = int(input())

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

for _ in range(t):
    n, r = list(map(int, input().split()))
    requests = list(map(int, input().split()))
    movie_to_idx = {}

    tree = FenwickTree(n + r + 1)
    for i in range(1, n + 1):
        movie_to_idx[n + 1 - i] = i
        tree.add(i, 1)

    sol = []
    next_idx = n + 1
    for req in requests:
        i = movie_to_idx[req]
        sol.append(n - tree.query(i))
        tree.add(i, -1)
        tree.add(next_idx, 1)
        movie_to_idx[req] = next_idx
        next_idx += 1

    print(' '.join(list(map(str, sol))))