r, c = list(map(int, input().split()))

board = []
for i in range(r):
    board.append(input().split())

for i in range(r):
    for j in range(c):
        if board[i][j] not in "tdTD-":
            board[i][j] = int(board[i][j])

t = int(input())
tiles = list(map(int, input().split()))
tiles.sort()

subsets = set()
for i in range(1, 2 ** t):
    arr = []
    idx = 0
    while i > 0:
        if i & 1:
            arr.append(tiles[idx])
        idx += 1
        i >>= 1
    subsets.add((tuple(arr), 0))
    subsets.add((tuple(arr[::-1]), 1))

best = 0

def run():
    global best
    r, c = len(board), len(board[0])
    for subset, decreasing in subsets:
        for i in range(r):
            for j in range(c):
                og_j = j
                if j > 0 and type(board[i][j - 1]) == int:
                    continue
                points = 0
                other_points = 0
                multiplier = 1
                placements = 0
                build = []
                works = True
                found = False
                while True:
                    if j >= c:
                        if placements != len(subset):
                            works = False
                        break
                    if type(board[i][j]) == int:
                        found = True
                        points += board[i][j]
                        build.append(board[i][j])
                    else:
                        if placements == len(subset):
                            break
                        num = subset[placements]
                        build.append(num)
                        val = num

                        curr_mod = 1
                        if board[i][j] == "T":
                            multiplier *= 3
                            curr_mod *= 3
                        elif board[i][j] == "D":
                            multiplier *= 2
                            curr_mod *= 2
                        elif board[i][j] == "d":
                            val *= 2
                        elif board[i][j] == "t":
                            val *= 3

                        points += val

                        above_col, below_col = 0, 0
                        above_order, below_order = -1, -1
                        if i > 0:
                            above_col = col_sums[i - 1][j][0]
                            above_order = col_sums[i - 1][j][1]
                        if i < r - 1:
                            below_col = col_sums[i + 1][j][0]
                            below_order = col_sums[i + 1][j][1]

                        if above_col > 0 or below_col > 0:
                            found = True
                            total_sum = val + above_col + below_col
                            if (total_sum * curr_mod) % 3 != 0:
                                works = False
                            other_points += total_sum * curr_mod

                        if above_col > 0 and below_col > 0:
                            if (above_order == 0 and below_order == 1) or (above_order == 1 and below_order == 0):
                                works = False
                            elif (above_order == 0 or below_order == 0):
                                works = works and (board[i - 1][j] <= num <= board[i + 1][j])
                            elif (above_order == 1 or below_order == 1):
                                works = works and (board[i - 1][j] >= num >= board[i + 1][j])
                            else:
                                works = works and ((board[i - 1][j] <= num <= board[i + 1][j]) or (board[i - 1][j] >= num >= board[i + 1][j]))
                        elif above_col > 0:
                            if above_order == 0 and num < board[i - 1][j]:
                                works = False
                            if above_order == 1 and num > board[i - 1][j]:
                                works = False
                        elif below_col > 0:
                            if below_order == 0 and num > board[i + 1][j]:
                                works = False
                            if below_order == 1 and num < board[i + 1][j]:
                                works = False

                        placements += 1

                    j += 1

                if decreasing and sorted(build, reverse=True) != build:
                    works = False
                if not decreasing and sorted(build) != build:
                    works = False
                if len(build) == 1:
                    works = False
                if points * multiplier % 3 != 0:
                    works = False
                
                if works and found:
                    best = max(best, points * multiplier + other_points)

def gen_col_sums():
    for j in range(c):
        curr = 0
        left = 0
        build = []
        for i in range(r):
            if type(board[i][j]) == int:
                curr += board[i][j]
                build.append(board[i][j])
            else:
                in_order = False
                out_order = False
                if sorted(build) == build:
                    in_order = True
                if sorted(build, reverse=True) == build:
                    out_order = True
                build = []
                num = (-1 if (in_order and out_order) else (1 if out_order else 0))
                for k in range(left, i):
                    col_sums[k][j] = (curr, num)
                curr = 0
                left = i + 1
        in_order = False
        out_order = False
        if sorted(build) == build:
            in_order = True
        if sorted(build, reverse=True) == build:
            out_order = True
        num = (-1 if (in_order and out_order) else (1 if out_order else 0))
        for k in range(left, r):
            col_sums[k][j] = (curr, num)

col_sums = [[(0, 0)] * c for _ in range(r)]
gen_col_sums()
run()

# switch everything
new_board = []
for j in range(c):
    arr = []
    for i in range(r):
        arr.append(board[i][j])
    new_board.append(arr)
board = new_board

r, c = c, r

col_sums = [[(0, 0)] * c for _ in range(r)]
gen_col_sums()
run()
print(best)