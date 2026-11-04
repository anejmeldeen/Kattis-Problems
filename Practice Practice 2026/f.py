from collections import deque

k, r = list(map(int, input().split()))
scores = list(map(int, input().split()))

parent = [x for x in range(3 * k + 1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b

for _ in range(r):
    a, b = list(map(int, input().split()))
    union(a, b)

groups = {}
for i, x in enumerate(parent):
    x = find(x)
    if i == 0:
        continue
    if x not in groups:
        groups[x] = [[], 0]
    groups[x][0].append(i)
    groups[x][1] += scores[i - 1]

sol = []
doubles = []
singles = []
impossible = False
for key in groups:
    arr, count = groups[key]
    if len(arr) == 3:
        sol.append(arr)
    elif len(arr) == 2:
        doubles.append((arr, count))
    elif len(arr) == 1:
        singles.append((arr, count))
    else:
        impossible = True

doubles.sort(key=lambda x: x[1], reverse=True)
singles.sort(key=lambda x: x[1], reverse=True)

doubles = deque(doubles)
singles = deque(singles)

while len(doubles) > 0 or len(singles) > 0:
    first_cost = 0
    if len(doubles) > 0 and len(singles) > 0:
        first_cost = doubles[0][1] + singles[0][1]

    second_cost = 0
    if len(singles) >= 3:
        second_cost = singles[0][1] + singles[1][1] + singles[2][1]

    if len(singles) - 3 < len(doubles):
        second_cost = 0

    if first_cost == 0 and second_cost == 0:
        impossible = True
        break
    if first_cost >= second_cost:
        sol.append(doubles[0][0] + singles[0][0])
        doubles.popleft()
        singles.popleft()
    else:
        sol.append(singles[0][0] + singles[1][0] + singles[2][0])
        singles.popleft()
        singles.popleft()
        singles.popleft()

if impossible:
    print("Impossible")
else:
    print("Possible")
    for row in sol:
        print(' '.join(list(map(str, row))))