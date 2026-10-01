r, c = list(map(int, input().split()))
board = []

for _ in range(r):
    board.append(input())

sol = []
for j in range(c):
    for i in range(r):
        if board[i][j] != ".":
            sol.append(board[i][j])
print(''.join(sol))