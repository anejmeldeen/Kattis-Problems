from collections import deque

n, m, s = list(map(int, input().split()))

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

found = False
queue = deque([(0, board[0][0], 0, 0)])
mini_costs = [[float('inf')] * m for _ in range(n)]
mini_costs[0][0] = 0

while queue:
    length, cost, x, y = queue.popleft()

    if x == n - 1 and y == m - 1:
        print(length)
        found = True
        break

    for xdir, ydir in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        newx, newy = x + xdir, y + ydir

        if newx < 0 or newy < 0 or newx >= n or newy >= m:
            continue

        new_cost = cost + board[newx][newy]
        if new_cost <= s and new_cost < mini_costs[newx][newy]:
            mini_costs[newx][newy] = new_cost
            queue.append((length + 1, new_cost, newx, newy))

if not found:
    print(-1)