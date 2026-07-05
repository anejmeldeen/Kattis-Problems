n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

change = True
impossible = False
while change:
    change = False
    for row in range(n - 1):
        for i in range(row + 1):
            top = board[row][i]
            left = board[row + 1][i]
            right = board[row + 1][i + 1]

            if top == 100 and left != 100 and right != 100:
                if left + right > 99 or left + right < -99:
                    impossible = True
                board[row][i] = left + right
                change = True
            elif left == 100 and top != 100 and right != 100:
                if top - right > 99 or top - right < -99:
                    impossible = True
                board[row + 1][i] = top - right
                change = True
            elif right == 100 and top != 100 and left != 100:
                if top - left > 99 or top - left < -99:
                    impossible = True
                board[row + 1][i + 1] = top - left
                change = True
            elif top != 100 and left != 100 and right != 100:
                if top != left + right:
                    impossible = True

        if impossible:
            break
    if impossible:
        break
        
ambig = False
for row in board:
    for item in row:
        if item == 100:
            ambig = True
            break

if impossible:
    print("no solution")
elif ambig:
    print("ambiguous")
else:
    print("solvable")
    for row in board:
        print(' '.join(list(map(str, row))))