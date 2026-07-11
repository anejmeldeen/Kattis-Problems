board = []
for _ in range(5):
    board.append(input())

def is_knight(x, y):
    if x >= 0 and x < 5 and y >= 0 and y < 5:
        return board[x][y] == "k"
    return False

def is_valid(x, y):
    return not (is_knight(x - 2, y - 1) or is_knight(x - 2, y + 1) or is_knight(x - 1, y + 2) or is_knight(x - 1, y - 2) or is_knight(x + 1, y - 2) or is_knight(x + 1, y + 2) or is_knight(x + 2, y - 1) or is_knight(x + 2, y + 1))    

k_count = 0
valid = True
for i in range(5):
    for j in range(5):
        if board[i][j] == "k":
            valid = valid and is_valid(i, j)
            k_count += 1

if valid and k_count == 9:
    print("valid")
else:
    print("invalid")