n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

change = True
impossible = False
while change and not impossible:
    change = False

    for i in range(len(board) - 1):
        for j in range(len(board[i])):
            top = board[i][j]
            bot_left = board[i + 1][j]
            bot_right = board[i + 1][j + 1]
            if top == 100 and bot_left != 100 and bot_right != 100:
                new = bot_left + bot_right
                board[i][j] = new
                if new >= 100 or new < -99:
                    impossible = True
                change = True
            elif top != 100 and bot_left == 100 and bot_right != 100:
                new = top - bot_right
                board[i + 1][j] = new
                if new >= 100 or new < -99:
                    impossible = True
                change = True
            elif top != 100 and bot_left != 100 and bot_right == 100:
                new = top - bot_left
                board[i + 1][j + 1] = new
                if new >= 100 or new < -99:
                    impossible = True
                change = True
            elif top != 100 and bot_left != 100 and bot_right != 100:
                if top != bot_left + bot_right:
                    impossible = True

ambig = False
for row in board:
    for ele in row:
        if ele == 100:
            ambig = True

if impossible:
    print("no solution")
elif ambig:
    print("ambiguous")
else:
    print("solvable")
    for row in board:
        print(' '.join(list(map(str, row))))