board = []
for _ in range(4):
    board.append(list(map(int, input().split())))

direction = int(input())

def solve(x):
    sol = []
    for val in x:
        if val == 0:
            continue
        sol.append(val)

    prev = -1
    real_sol = []
    for val in sol:
        if val == prev:
            real_sol[-1] *= 2
            prev = -1
        else:
            real_sol.append(val)
            prev = val

    return real_sol + [0] * (4 - len(real_sol))

if direction == 0:
    for row in board:
        res = solve(row)
        for i in range(4):
            row[i] = res[i]
elif direction == 1:
    for j in range(4):
        row = [board[i][j] for i in range(4)]
        res = solve(row)
        for i in range(4):
            board[i][j] = res[i]
elif direction == 2:
    for row in board:
        res = solve(row[::-1])
        for i in range(4):
            row[3 - i] = res[i]
else:
    for j in range(4):
        row = [board[i][j] for i in range(3, -1, -1)]
        res = solve(row)
        for i in range(4):
            board[3 - i][j] = res[i]

for row in board:
    print(' '.join(list(map(str, row))))