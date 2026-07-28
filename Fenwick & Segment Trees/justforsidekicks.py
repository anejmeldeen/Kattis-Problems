n, q = list(map(int, input().split()))
values = list(map(int, input().split()))

class SegmentTree:
    def __init__(self, data):
        self.orig_n = len(data)
        self.n = 1
        while self.n < self.orig_n: self.n <<= 1

        self.tree = [None] * (2 * self.n)
        for i in range(self.orig_n):
            self.tree[self.n + i] = data[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[i << 1], self.tree[i << 1 | 1])

    def merge(self, left, right):
        if left is None: return right
        if right is None: return left
        new = [left[i] + right[i] for i in range(6)]
        return tuple(new)

    def update(self, p, value):
        p += self.n
        self.tree[p] = value
        while p > 1:
            left_node = self.tree[min(p, p^1)]
            right_node = self.tree[max(p, p^1)]
            self.tree[p >> 1] = self.merge(left_node, right_node)
            p >>= 1

    def query(self, l, r):
        l += self.n
        r += self.n
        res_l = None
        res_r = None
        while l <= r:
            if l & 1:
                res_l = self.merge(res_l, self.tree[l])
                l += 1
            if not (r & 1):
                res_r = self.merge(self.tree[r], res_r)
                r -= 1
            l >>= 1
            r >>= 1
        return self.merge(res_l, res_r)

nums = input()
data = []
for char in nums:
    res = [0] * 6
    num = int(char)
    res[num - 1] += 1
    data.append(tuple(res))

segtree = SegmentTree(data)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        new = [0] * 6
        new[query[2] - 1] += 1
        segtree.update(query[1] - 1, tuple(new))
    elif query[0] == 2:
        values[query[1] - 1] = query[2]
    elif query[0] == 3:
        res = segtree.query(query[1] - 1, query[2] - 1)
        count = 0
        for i in range(6):
            count += values[i] * res[i]
        print(count)