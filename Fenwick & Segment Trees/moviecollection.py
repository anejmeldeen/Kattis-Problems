t = int(input())
for _ in range(t):
    m, r = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    bit = [0] * (r + m + 1)
    def add(idx, val):
        while idx <= r + m:
            bit[idx] += val
            idx += idx & -idx
    def query(idx):
        total = 0
        while idx > 0:
            total += bit[idx]
            idx -= idx & -idx
        return total

    mappy = {i: r + i for i in range(1, m + 1)}
    for key in mappy:
        add(mappy[key], 1)

    curr = r
    res = []
    for num in queries:
        res.append(query(mappy[num]) - 1)
        add(mappy[num], -1)
        mappy[num] = curr
        add(curr, 1)
        curr -= 1

    print(' '.join(list(map(str, res))))