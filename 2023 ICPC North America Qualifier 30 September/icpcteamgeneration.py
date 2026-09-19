from collections import deque

n = int(input())
queue = deque()

sol = 0
for r in range(1, n + 1):
    a, b = list(map(int, input().split()))
    while queue and not (queue[0][1] >= r and a <= queue[0][2]):
        queue.popleft()
    queue.append((a, b, r))

    if len(queue) == 3:
        queue = deque()
        sol += 1

print(sol)