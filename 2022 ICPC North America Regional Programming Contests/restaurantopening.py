n, m = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

row_sums = []
col_sums = []

for j in range(m):
    summ = 0
    for i in range(n):
        summ += board[i][j]
    row_sums.append(summ)

for i in range(n):
    summ = 0
    for j in range(m):
        summ += board[i][j]
    col_sums.append(summ)

optimal_x = 0
curr = 0
need = sum(row_sums) / 2
while curr < need:
    curr += row_sums[optimal_x]
    optimal_x += 1

optimal_y = 0
curr = 0
need = sum(col_sums) / 2
while curr < need:
    curr += col_sums[optimal_y]
    optimal_y += 1

optimal_x -= 1
optimal_y -= 1

sol = 0
for x in range(n):
    for y in range(m):
        sol += (abs(x - optimal_y) + abs(y - optimal_x)) * board[x][y]
print(sol)