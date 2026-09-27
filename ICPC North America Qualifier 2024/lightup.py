n = int(input())

board = []
for _ in range(n):
    board.append(input())

works = True

lit = set()

for i in range(n):
    for j in range(n):
        if board[i][j] == "?":
            # north
            for x in range(i - 1, -1, -1):
                if board[x][j] == "?":
                    works = False
                    break
                elif board[x][j] == ".":
                    lit.add((x, j))
                else:
                    break

            # south
            for x in range(i + 1, n):
                if board[x][j] == "?":
                    works = False
                    break
                elif board[x][j] == ".":
                    lit.add((x, j))
                else:
                    break

            # east
            for y in range(j + 1, n):
                if board[i][y] == "?":
                    works = False
                    break
                elif board[i][y] == ".":
                    lit.add((i, y))
                else:
                    break

            # west
            for y in range(j - 1, -1, -1):
                if board[i][y] == "?":
                    works = False
                    break
                elif board[i][y] == ".":
                    lit.add((i, y))
                else:
                    break

        if board[i][j] not in "?.X":
            num = int(board[i][j])
            count = 0
            for xdir, ydir in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                newx = i + xdir
                newy = j + ydir
                if newx < 0 or newy < 0 or newx >= n or newy >= n:
                    continue
                if board[newx][newy] == "?":
                    count += 1
            if num != count:
                works = False

for i in range(n):
    for j in range(n):
        if board[i][j] == "." and (i, j) not in lit:
            works = False

print(1 if works else 0)