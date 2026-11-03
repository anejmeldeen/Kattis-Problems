board = []
for _ in range(9):
    board.append(list(input().split()))

number_set = set("123456789")

change = True
while change:
    change = False

    # single value rule
    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    square_set = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            square = i // 3 * 3 + j // 3
            if board[i][j] != "0":
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                square_set[square].add(board[i][j])

    for i in range(9):
        for j in range(9):
            square = i // 3 * 3 + j // 3
            row_col = row_set[i] | col_set[j] | square_set[square]
            rem = number_set.difference(row_col)
            if board[i][j] != "0":
                continue
            if len(rem) == 1:
                board[i][j] = rem.pop()
                change = True
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                square_set[square].add(board[i][j])

    # unique location rule
    for i in range(9):
        for num in "123456789":
            if num in row_set[i]:
                continue
            cands = []
            for j in range(9):
                square = i // 3 * 3 + j // 3
                if board[i][j] != "0":
                    continue
                if num in col_set[j]:
                    continue
                if num in square_set[square]:
                    continue
                cands.append(j)
            if len(cands) == 1:
                loc = cands.pop()
                board[i][loc] = num
                row_set[i].add(board[i][loc])
                col_set[loc].add(board[i][loc])
                square_set[i // 3 * 3 + loc // 3].add(board[i][loc])
                change = True

    for j in range(9):
        for num in "123456789":
            if num in col_set[j]:
                continue
            cands = []
            for i in range(9):
                square = i // 3 * 3 + j // 3
                if board[i][j] != "0":
                    continue
                if num in row_set[i]:
                    continue
                if num in square_set[square]:
                    continue
                cands.append(i)
            if len(cands) == 1:
                loc = cands.pop()
                board[loc][j] = num
                row_set[loc].add(board[loc][j])
                col_set[j].add(board[loc][j])
                square_set[loc // 3 * 3 + j // 3].add(board[loc][j])
                change = True

    for square in range(9):
        for num in "123456789":
            if num in square_set[square]:
                continue
            i = square // 3
            j = square % 3
            cands = []
            for x in range(i * 3, i * 3 + 3):
                for y in range(j * 3, j * 3 + 3):
                    if board[x][y] != "0":
                        continue
                    if num in row_set[x]:
                        continue
                    if num in col_set[y]:
                        continue
                    cands.append((x, y))
            if len(cands) == 1:
                loc = cands.pop()
                i, j = loc
                board[i][j] = num
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                square_set[i // 3 * 3 + j // 3].add(board[i][j])
                change = True

solved = True
for row in board:
    for i, char in enumerate(row):
        if char == "0":
            row[i] = "."
            solved = False

print("Easy" if solved else "Not easy")
for row in board:
    print(' '.join(row))