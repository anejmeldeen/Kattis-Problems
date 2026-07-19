from collections import deque

n, m, k = list(map(int, input().split()))

memory = set()
currency = -1
for i in range(n):
    if i == k - 1:
        currency = int(input())
    else:
        memory.add(int(input()))

operations = []
for _ in range(m):
    data = input().split()
    data[1] = int(data[1])
    operations.append(data)

parent = {}

seen = set([currency])
res = -1
last = -1
queue = deque()
queue.append((currency, 0))
while queue:
    data = queue.popleft()
    curr = data[0]
    cost = data[1]

    if curr not in memory:
        res = cost
        last = curr
        break

    for i, oper in enumerate(operations):
        op = oper[0]
        num = oper[1]

        if op == "+":
            new = curr + num
        elif op == "-":
            new = curr - num
        elif op == "*":
            new = curr * num
        elif op == "/":
            new = curr // num

        if new in seen or new < 0:
            continue
        parent[new] = (curr, i + 1)
        seen.add(new)
        queue.append((new, cost + 1))

print(res)
rev = []
while last in parent:
    data = parent[last]
    last = data[0]
    rev.append(data[1])
for i in range(len(rev) - 1, -1, -1):
    print(rev[i])