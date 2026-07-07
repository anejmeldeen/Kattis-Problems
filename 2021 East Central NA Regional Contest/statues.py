n, m = list(map(int, input().split()))
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

height_to_loc = {}
vals = []

empty = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            empty[i][j] = -1
        else:
            height_to_loc[board[i][j]] = (i, j)
            vals.append(board[i][j])

vals.sort()

sol = float('inf')

def solve(lower, upper, shift, func):
    global sol
    count = 0
    idx = 0
    for summy in range(lower, upper, shift):
        old_locs = []
        new_locs = set()
        for i in range(n):
            j = func(summy, i)
            if j < 0 or j >= m:
                continue
            if empty[i][j] != -1:
                move_loc = height_to_loc[vals[idx]]
                new_locs.add((i, j))
                old_locs.append(move_loc)
                idx += 1
        
        add = len(new_locs)
        for loc in old_locs:
            if loc in new_locs:
                add -= 1
        count += add

    sol = min(sol, count)

def func1(x, y):
    return x - y

def func2(x, y):
    return -x + y

solve(0, n + m - 1, 1, func1)
solve(n + m - 2, -1, -1, func1)
solve(n - 1, -m, -1, func2)
solve(-m + 1, n, 1, func2)

print(sol)