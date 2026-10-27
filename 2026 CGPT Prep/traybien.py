from functools import cache

m, n = list(map(int, input().split()))

bad = set()

locs = list(map(float, input().split())) if n > 0 else []
for i in range(0, 2 * n, 2):
    bad.add((int(locs[i + 1]), int(locs[i])))

@cache
def recurse(data):
    res = list(data)
    for i in range(3):
        while (i, res[i]) in bad:
            res[i] += 1

    top, mid, bot = res
    mini = min(res)
    if top == mini:
        curr = 0
    elif mid == mini:
        curr = 1
    else:
        curr = 2

    if top == m and mid == m and bot == m:
        return 1
    
    total = 0
    res[curr] += 1
    total += recurse(tuple(res))
    res[curr] -= 1

    if curr < 2 and res[curr] == res[curr + 1]:
        res[curr] += 1
        res[curr + 1] += 1
        total += recurse(tuple(res))
        res[curr] -= 1
        res[curr + 1] -= 1

    if res[curr] < m - 1 and (curr, res[curr] + 1) not in bad:
        res[curr] += 2
        total += recurse(tuple(res))
        res[curr] -= 2

    return total

print(recurse((0, 0, 0)))