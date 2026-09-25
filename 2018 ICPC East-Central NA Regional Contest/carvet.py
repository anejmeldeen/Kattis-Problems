import sys
sys.setrecursionlimit(int(1e9))

n, m = list(map(int, input().split()))

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

x, y = list(map(int, input().split()))

sol_arr = []
def move(x, y, path, seen):
    global sol_arr

    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    curr_num = board[x][y]
    if curr_num in seen or curr_num == -2:
        return False
    if curr_num == -1:
        sol_arr = path.copy()
        return True
    
    real_xdir, real_ydir = -1, -1
    for xdir, ydir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        new_x = x + xdir
        new_y = y + ydir
        if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
            continue
        if board[new_x][new_y] == curr_num:
            real_xdir = xdir
            real_ydir = ydir

    seen.add(curr_num)
    path.append(curr_num)
    res = move(x + real_xdir * 2, y + real_ydir * 2, path, seen)
    seen.remove(curr_num)
    path.pop()
    return res


arr = []
res = move(x - 1, y - 1, arr, set())

if res:
    print(' '.join(list(map(str, sol_arr[::-1]))))
else:
    print("impossible")