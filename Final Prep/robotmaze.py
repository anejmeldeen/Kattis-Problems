from collections import deque

t = int(input())
for _ in range(t):
    input()
    r, c = list(map(int, input().split()))
    board = []
    for _ in range(r):
        board.append(list(input()))

    start = -1, -1
    dest = -1, -1
    for i in range(r):
        for j in range(c):
            if board[i][j] == "R":
                start = i, j
            elif board[i][j] == "D":
                dest = i, j

    seen = set()
    queue = deque([(0, start[0], start[1], -1, -1)])
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    found = False
    while queue:
        cost, x, y, prev, double = queue.popleft()
        seen.add((x, y, prev, double))

        if dest[0] == x and dest[1] == y:
            found = True
            print(cost)
            break

        for i, dirdir in enumerate(dirs):
            if (i + 2) % 4 == prev:
                continue
            xdir, ydir = dirdir
            newx = x + xdir
            newy = y + ydir

            if double == 1 and i == prev:
                continue
            new_double = 1 if i == prev else 0
            if newx < 0 or newy < 0 or newx >= r or newy >= c or (newx, newy, i, new_double) in seen:
                continue
            if board[newx][newy] == "B":
                continue
            seen.add((newx, newy, i, new_double))
            queue.append((cost + 1, newx, newy, i, new_double))

    if not found:
        print(-1)