r, c = list(map(int, input().split()))
board = []

for _ in range(r):
    board.append(list(input()))

key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

ids = [["."] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j] == "#":
            ids[i][j] = "#"

def recurse(placements):
    use_i, use_j = -1, -1
    for i in range(r):
        for j in range(c):
            if ids[i][j] == ".":
                use_i = i
                use_j = j
                break
        if use_i != -1:
            break

    if use_i == -1:
        for row in ids:
            print(''.join(row))
        exit()
    i, j = use_i, use_j
    length = 0
    if ids[i][j] == ".":
        works = True
        found_treasures = 0
        while works:
            length += 1
            if i + length - 1 >= r or j + length - 1 >= c:
                break
            for k in range(i, i + length):
                if board[k][j + length - 1] == "$":
                    found_treasures += 1
                if ids[k][j + length - 1] != ".":
                    works = False
            for k in range(j, j + length - 1):
                if board[i + length - 1][k] == "$":
                    found_treasures += 1
                if ids[i + length - 1][k] != ".":
                    works = False
            if not works or found_treasures > 1:
                break
            for k in range(i, i + length):
                ids[k][j + length - 1] = key[placements]
            for k in range(j, j + length):
                ids[i + length - 1][k] = key[placements]
            if found_treasures == 1:
                recurse(placements + 1)
    for k in range(i, i + length - 1):
        for l in range(j, j + length - 1):
            ids[k][l] = "."

recurse(0)
print("elgnatcer")