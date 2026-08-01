import sys
sys.setrecursionlimit(int(1e9))

from functools import cache

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

def tuple_to_board(tuple):
    board = []
    idx = 0
    for i in range(5):
        row = []
        for _ in range(i + 1):
            row.append(tuple[idx])
            idx += 1
        board.append(row)
    return board

def board_to_tuple(board):
    tuply = []
    for row in board:
        for ele in row:
            tuply.append(ele)
    return tuple(tuply)

@cache
def recurse(board):
    board = tuple_to_board(board)
    best = -float('inf')
    for j, row in enumerate(board):
        for i, ele in enumerate(row):
            if ele == 0:
                points = [((i - 1, j), (i - 2, j)),
                          ((i + 1, j), (i + 2, j)),
                          ((i, j - 1), (i, j - 2)),
                          ((i - 1, j - 1), (i - 2, j - 2)),
                          ((i, j + 1), (i, j + 2)),
                          ((i + 1, j + 1), (i + 2, j + 2))]

                for pt1, pt2 in points:
                    x1, y1 = pt1
                    x2, y2 = pt2
                    if y1 < 0 or y1 >= 5 or y2 < 0 or y2 >= 5 or x1 < 0 or x2 < 0 or x1 >= len(board[y1]) or x2 >= len(board[y2]) or board[y1][x1] == 0 or board[y2][x2] == 0:
                        continue

                    new_board = [x.copy() for x in board]
                    score = new_board[y1][x1] * new_board[y2][x2]
                    new_board[j][i] = new_board[y2][x2]
                    new_board[y2][x2] = 0
                    new_board[y1][x1] = 0                    

                    score -= recurse(board_to_tuple(new_board))
                    best = max(best, score)

    if best == float('-inf'):
        return 0
    return best

print(recurse(board_to_tuple(board)))