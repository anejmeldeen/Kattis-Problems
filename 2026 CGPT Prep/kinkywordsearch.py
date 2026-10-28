from functools import cache

r, c = list(map(int, input().split()))
board = []

for _ in range(r):
    board.append(input().split())

k = int(input())
word = input()

if k >= len(word):
    print("No")
    exit()

dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]

@cache
def recurse(idx, i, j, kinks, p_dir):
    if i < 0 or j < 0 or i >= r or j >= c or kinks < 0 or idx >= len(word) or word[idx] != board[i][j] or len(word) - idx < kinks:
        return
    if idx == len(word) - 1 and kinks == 0:
        print("Yes")
        exit()

    for d in range(8):
        new_kinks = kinks - 1
        if d == p_dir or p_dir == -1:
            new_kinks = kinks
        recurse(idx + 1, i + dirs[d][0], j + dirs[d][1], new_kinks, d)

for i in range(r):
    for j in range(c):
        recurse(0, i, j, k, -1)

print("No")