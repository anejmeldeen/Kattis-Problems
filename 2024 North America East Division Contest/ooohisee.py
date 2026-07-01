r, c = list(map(int, input().split()))
board = []
for _ in range(r):
    board.append(input())

count = 0
x, y = -1, -1
for i in range(1, r - 1):
    for j in range(1, c - 1):
        if board[i][j] == '0' and board[i - 1][j] == 'O' and board[i + 1][j] == 'O' and board[i - 1][j - 1] == 'O' and board[i - 1][j + 1] == 'O' and board[i][j - 1] == 'O' and board[i][j + 1] == 'O' and board[i + 1][j - 1] == 'O' and board[i + 1][j + 1] == 'O':
            count += 1
            x, y = i + 1, j + 1

if count == 1:
    print(x, y)
elif count > 1:
    print(f"Oh no! {count} locations")
else:
    print("Oh no!")