r, c = list(map(int, input().split()))
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

s, t = list(map(int, input().split()))
office = []
for _ in range(s):
    office.append(list(input()))

def solve(board, office):
    r, c = len(board), len(board[0])
    s, t = len(office), len(office[0])

    best = float('inf')
    for i in range(r - s + 1):
        for j in range(c - t + 1):
            curr = 0
            for x in range(i, i + s):
                for y in range(j, j + t):
                    if office[x - i][y - j] == "#":
                        curr += board[x][y]
            best = min(best, curr)
    
    return best

def rotate_clockwise(matrix):
    new_matrix = []
    for j in range(len(matrix[0])):
        new = []
        for i in range(len(matrix) - 1, -1, -1):
            new.append(matrix[i][j])
        new_matrix.append(new)
    return new_matrix

total_sum = sum([sum(row) for row in board])
best = float('inf')
best = min(best, solve(board, office))
office = rotate_clockwise(office)
best = min(best, solve(board, office))
office = rotate_clockwise(office)
best = min(best, solve(board, office))
office = rotate_clockwise(office)
best = min(best, solve(board, office))

print(total_sum - best)