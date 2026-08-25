n = int(input())
for _ in range(n):
    board = [[""] * 3 for _ in range(3)]
    state = int(input(), 8)

    taken = [[False] * 3 for _ in range(3)]
    for curr in range(9):
        if state & 1:
            taken[curr // 3][curr % 3] = True
        state >>= 1

    for curr in range(9):
        if taken[curr // 3][curr % 3]:
            if state & 1:
                board[curr // 3][curr % 3] = "X"
            else:
                board[curr // 3][curr % 3] = "O"
        state >>= 1

    winner = -1
    empty_spot = False
    for row in board:
        if "" in row:
            empty_spot = True

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            winner = f"{row[0]} wins"
            break

    for j in range(3):
        row = [board[i][j] for i in range(3)]
        if row[0] == row[1] == row[2] and row[0] != "":
            winner = f"{row[0]} wins"
            break

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        winner = f"{board[0][0]} wins"

    if board[2][0] == board[1][1] == board[0][2] and board[0][2] != "":
        winner = f"{board[1][1]} wins"

    if winner == -1:
        if empty_spot:
            print("In progress")
        else:
            print("Cat's")
    else:
        print(winner)