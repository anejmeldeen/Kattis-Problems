import math

r, c = list(map(int, input().split()))
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

num_zeroes = 0
num_ones = 0
num_twos = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            num_zeroes += 1
        elif board[i][j] == 2:
            num_twos += 1
        else:
            num_ones += 1

if num_zeroes >= 2:
    print(0)
elif num_zeroes == 0:
    larger = math.ceil(num_twos / 2)
    smaller = math.floor(num_twos / 2)
    print(2 ** larger - 2 ** smaller)
else:
    if r >= 2 and c >= 2:
        if num_ones:
            print(1)
        else:
            print(2)
    else:
        val1 = board[0][0]
        val2 = board[-1][-1]

        if val1 == 0:
            print(val2)
        elif val2 == 0:
            print(val1)
        else:
            print(min(val1, val2))