r, c = list(map(int, input().split()))
board = []
for _ in range(r):
    board.append(input())

def manachers(s):
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n
    c = 0
    r = 0

    for i in range(1, n - 1):
        mirror = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mirror])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > r:
            c = i
            r = i + p[i]

    return p

horizontal_matrix = [[0] * c for _ in range(r)]
vertical_matrix = [[0] * c for _ in range(r)]

for row in range(r):
    p = manachers(board[row])
    for i in range(2, len(p) - 2):
        L = p[i]
        if L == 0:
            continue

        start_idx = (i - L - 1) // 2
        end_idx = (i + L - 3) // 2

        for col in range(start_idx, end_idx + 1):
            horizontal_matrix[row][col] = max(horizontal_matrix[row][col], L)

for col in range(c):
    row = ''.join(board[i][col] for i in range(r))
    p = manachers(row)
    for i in range(2, len(p) - 2):
            L = p[i]
            if L == 0:
                continue
    
            start_idx = (i - L - 1) // 2
            end_idx = (i + L - 3) // 2
    
            for row in range(start_idx, end_idx + 1):
                vertical_matrix[row][col] = max(vertical_matrix[row][col], L)

best = 0
for i in range(r):
    for j in range(c):
        best = max(best, horizontal_matrix[i][j] * vertical_matrix[i][j])
print(best)