from functools import cache
from collections import deque

rows = []
works = True
maxi = 0

for _ in range(3):
    arr = list(map(int, input().split()[1:]))

    if arr != sorted(arr, reverse=True):
        works = False

    rows.append(tuple(arr))

    if len(arr) > 0:
        maxi = max(maxi, max(arr))

rows = tuple(rows)

if not works:
    print("No")
    exit()

@cache
def recurse(rows, n, loc):
    rows = tuple([list(row) for row in rows])

    cost = 0
    if n == 0:
        return 0

    find = -1
    for i in range(3):
        if len(rows[i]) > 0 and rows[i][0] == n:
            find = i

    rows[find].pop(0)

    rows = tuple([tuple(row) for row in rows])

    if find == loc:
        cost = recurse(rows, n - 1, loc)
    else:
        cost += 2 ** (n - 1)

        new_loc = [0, 1, 2]
        new_loc.remove(find)
        if loc in new_loc:
            new_loc.remove(loc)

        best = float('inf')
        for item in new_loc:
            best = min(best, recurse(rows, n - 1, item))
        cost += best

    return cost

forward_cost = recurse(rows, maxi, 2)
backward_cost = recurse(rows, maxi, 0)

if forward_cost + backward_cost == (2 ** maxi) - 1:
    print(forward_cost)
else:
    print("No")