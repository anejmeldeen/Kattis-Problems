board = []
for _ in range(8):
    board.append(input())

allowed = True
locs = []

for i in range(8):
    for j in range(8):
        if board[i][j] == "*":
            locs.append((i, j))

x_coords = [pair[0] for pair in locs]
y_coords = [pair[1] for pair in locs]
sums = [sum(pair) for pair in locs]
difs = [pair[1] - pair[0] for pair in locs]

if len(set(x_coords)) != 8:
    allowed = False
if len(set(y_coords)) != 8:
    allowed = False
if len(set(sums)) != 8:
    allowed = False
if len(set(difs)) != 8:
    allowed = False

if allowed:
    print("valid")
else:
    print("invalid")