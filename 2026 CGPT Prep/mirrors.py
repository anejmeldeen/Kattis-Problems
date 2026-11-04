n, c, r = list(map(int, input().split()))
board = []

for _ in range(n):
    board.append(list(input().split()))

choices = [[-1, 0], [0, 1], [1, 0], [0, -1]]
good = set()

last = (r - 1, n - 1, 3)
while True:
    x, y, my_dir = last
    if x < 0 or y < 0 or x >= n or y >= n:
        break
    good.add((x, y, (my_dir + 2) % 4))
    if board[x][y] == "/":
        if my_dir in [1, 3]:
            my_dir = (my_dir - 1) % 4
        else:
            my_dir = (my_dir + 1) % 4
    elif board[x][y] == "\\":
        if my_dir in [0, 2]:
            my_dir = (my_dir - 1) % 4
        else:
            my_dir = (my_dir + 1) % 4
    choice = choices[my_dir]
    last = (x + choice[0], y + choice[1], my_dir)

last = (0, c - 1, 2)
works = False

while True:
    x, y, my_dir = last
    if x < 0 or y < 0 or x >= n or y >= n:
        break
    if board[x][y] == "/":
        if my_dir in [1, 3]:
            my_dir = (my_dir - 1) % 4
        else:
            my_dir = (my_dir + 1) % 4
    elif board[x][y] == "\\":
        if my_dir in [0, 2]:
            my_dir = (my_dir - 1) % 4
        else:
            my_dir = (my_dir + 1) % 4

    if (x, y, my_dir) in good:
        works = True
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == "." and ((x, y, (my_dir + 1) % 4) in good or (x, y, (my_dir - 1) % 4) in good):
        works = True

    choice = choices[my_dir]
    last = (x + choice[0], y + choice[1], my_dir)

print("YES" if works else "NO")