m, n = list(map(int, input().split()))
board = []

for _ in range(m):
    board.append(list(map(int, input().split())))

dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

x, y = list(map(int, input().split()))
x -= 1
y -= 1

path = []
seen = set()
while True:
    if x < 0 or y < 0 or x >= m or y >= n or board[x][y] == -2:
        print("impossible")
        exit()
    if board[x][y] == -1:
        break
    num = board[x][y]
    if num in seen:
        print("impossible")
        exit()
    the_dir = -1
    for i, dir_pair in enumerate(dirs):
        new_x, new_y = x + dir_pair[0], y + dir_pair[1]
        if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or board[new_x][new_y] != num:
            continue
        the_dir = i

    path.append(num)
    seen.add(num)
    x, y = x + dirs[the_dir][0] * 2, y + dirs[the_dir][1] * 2

print(' '.join(list(map(str, path[::-1]))))