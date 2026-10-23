from functools import cache

r, c = list(map(int, input().split()))
board = []
for _ in range(r):
    board.append(input().split())

k = int(input())
word = input()

dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

@cache
def search(idx, i, j, kinks, prev_dir=8):
    if kinks > len(word) - idx:
        return False
    if idx == len(word) - 1:
        return kinks == 0
    if kinks < 0:
        return False

    ret = False
    for dirdir, dire in enumerate(dirs):
        xdir, ydir = dire
        new_kinks = kinks
        if prev_dir != 8 and prev_dir != dirdir:
            new_kinks -= 1

        new_x = i + xdir
        new_y = j + ydir
        if new_x < 0 or new_y < 0 or new_x >= r or new_y >= c or word[idx + 1] != board[new_x][new_y]:
            continue
        ret = ret or search(idx + 1, i + xdir, j + ydir, new_kinks, dirdir)

    return ret

can = False
for i in range(r):
    for j in range(c):
        if board[i][j] == word[0]:
            can = can or search(0, i, j, k)

print("Yes" if can else "No")