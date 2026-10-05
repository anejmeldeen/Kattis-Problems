from collections import deque

m = int(input())
costs = list(map(int, input().split()))

queue = deque()

n, e = list(map(int, input().split()))
for _ in range(e):
    time, person = list(map(int, input().split()))
    queue.append((time, person))

table = [-1] * (n + 1)
curr = 0

sol = [0] * n

for time in range(10001):
    if table[0] == -1:
        table[0] = costs[curr]
        curr += 1
        curr %= m

    while queue and queue[0][0] <= time:
        time, person = queue.popleft()
        sol[person - 1] += table[person]
        table[person] = -1

    # move table
    table = [table[-1]] + table[:-1]

for ele in sol:
    print(ele)