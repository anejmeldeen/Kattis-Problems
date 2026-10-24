n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

imposs = False
ambig = False
change = True
while change and not imposs:
    change = False

    for i in range(n - 1):
        for j in range(i + 1):
            top = board[i][j]
            bot_left = board[i + 1][j]
            bot_right = board[i + 1][j + 1]
            if top != 100 and bot_left != 100 and bot_right != 100:
                if top != bot_left + bot_right:
                    imposs = True
            elif top != 100 and bot_left != 100 and bot_right == 100:
                new_val = top - bot_left
                if new_val < -99 or new_val > 99:
                    imposs = True
                change = True
                board[i + 1][j + 1] = new_val
            elif top == 100 and bot_left != 100 and bot_right != 100:
                new_val = bot_left + bot_right
                if new_val < -99 or new_val > 99:
                    imposs = True
                change = True
                board[i][j] = new_val
            elif top != 100 and bot_left == 100 and bot_right != 100:
                new_val = top - bot_right
                if new_val < -99 or new_val > 99:
                    imposs = True
                change = True
                board[i + 1][j] = new_val

for row in board:
    for num in row:
        if num == 100:
            ambig = True

if imposs:
    print("no solution")
elif ambig:
    print("ambiguous")
else:
    print("solvable")
    for row in board:
        print(' '.join(list(map(str, row))))