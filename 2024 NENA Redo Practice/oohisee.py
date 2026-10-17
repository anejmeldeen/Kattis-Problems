r, c = list(map(int, input().split()))
board = []

for _ in range(r):
    board.append(input())

x, y = -1, -1
loc_count = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == "0":
            count = 0
            for xdir, ydir in [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, -1], [0, 1]]:
                newi = i + xdir
                newj = j + ydir
                if newi < 0 or newj < 0 or newi >= r or newj >= c or board[newi][newj] != "O":
                    continue
                count += 1
            if count == 8:
                loc_count += 1
                x = i
                y = j

if loc_count == 0:
    print("Oh no!")
elif loc_count > 1:
    print(f"Oh no! {loc_count} locations")
else:
    print(x + 1, y + 1)