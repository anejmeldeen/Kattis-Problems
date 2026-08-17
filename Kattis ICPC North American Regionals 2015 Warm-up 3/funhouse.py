test_no = 0
while (data := input()) != "0 0":
    w, l = list(map(int, data.split()))
    test_no += 1
    board = []
    
    for _ in range(l):
        board.append(list(input()))

    x = y = -1
    direction = 0
    for i in range(l):
        for j in range(w):
            if board[i][j] == "*":
                x, y = i, j
                if x == 0:
                    direction = 2
                elif x == l - 1:
                    direction = 0
                elif y == 0:
                    direction = 1
                elif y == w - 1:
                    direction = 3

    while board[x][y] != "x":
        if direction == 0:
            x -= 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x += 1
        else:
            y -= 1

        if board[x][y] == "/":
            if direction in [1, 3]:
                direction -= 1
                direction %= 4
            else:
                direction += 1
                direction %= 4
        elif board[x][y] == "\\":
            if direction in [1, 3]:
                direction += 1
                direction %= 4
            else:
                direction -= 1
                direction %= 4

    board[x][y] = "&"

    print(f"HOUSE {test_no}")
    for row in board:
        print(''.join(row))