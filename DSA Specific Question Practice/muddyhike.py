import heapq

r, c = list(map(int, input().split()))

board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

seen = [[False] * c for _ in range(r)]
heap = []

for i in range(r):
    heapq.heappush(heap, (board[i][0], i, 0))

while heap:
    data = heapq.heappop(heap)
    cost, x, y = data

    if seen[x][y]:
        continue
    seen[x][y] = True
    if y == c - 1:
        print(cost)
        break

    for xdir, ydir in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        new_x = x + xdir
        new_y = y + ydir
        if new_x < 0 or new_y < 0 or new_x >= r or new_y >= c or seen[new_x][new_y]:
            continue
        heapq.heappush(heap, (max(board[new_x][new_y], cost), new_x, new_y))