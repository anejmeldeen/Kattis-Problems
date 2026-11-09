from collections import deque, defaultdict

n = int(input())
board = []
for _ in range(2 * n + 1):
    board.append(list(input()))

matrix = []
for i in range(1, 2 * n, 2):
    arr = []
    for j in range(1, 2 * n, 2):
        if board[i][j] == "o":
            arr.append(True)
        else:
            arr.append(False)
    matrix.append(arr)

in_degree = defaultdict(int)
connects_to = defaultdict(list)
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
queue = deque()

num_offices = 0
count = 0
for i in range(n):
    for j in range(n):
        if not matrix[i][j]:
            continue
        num_offices += 1
        key = i * n + j
        for p, dirdir in enumerate(dirs):
            idir, jdir = dirdir
            newi = i + idir
            newj = j + jdir
            if newi < 0 or newj < 0 or newi >= n or newj >= n:
                continue
            if matrix[newi][newj]:
                connects_to[key].append((newi * n + newj, p))
                in_degree[key] += 1
        if in_degree[key] == 1:
            queue.append((key, -1))

mappy = {}
while queue:
    count += 1
    key, prev = queue.popleft()
    i = key // n
    j = key % n
    matrix[i][j] = False
    if in_degree[key] == 0:
        continue

    for data in connects_to[key]:
        item, dirdir = data
        if item == prev:
            continue
        in_degree[item] -= 1
        if in_degree[item] == 1:
            queue.append((item, key))
        mappy[key] = dirdir

def dfs(key, first):
    i = key // n
    j = key % n
    if in_degree[key] >= 3:
        print("impossible")
        exit()
    matrix[i][j] = False

    if first:
        mappy[key] = 3
        mappy[key + n] = 0
        dfs(key + 1, False)
    else:
        for conn, p in connects_to[key]:
            conn_i = conn // n
            conn_j = conn % n
            if matrix[conn_i][conn_j]:
                dfs(conn, False)
                mappy[key] = p

for i in range(n):
    for j in range(n):
        if matrix[i][j] and in_degree[i * n + j] != 0:
            dfs(i * n + j, True)

panels = 0
for x in range(n):
    for y in range(n):
        key = x * n + y
        i = 1 + 2 * x
        j = 1 + 2 * y
        if key in mappy:
            panels += 1
            dirdir = mappy[key]
            if dirdir == 0:
                board[i - 1][j] = "v"
            elif dirdir == 1:
                board[i + 1][j] = "^"
            elif dirdir == 2:
                board[i][j - 1] = ">"
            else:
                board[i][j + 1] = "<"

print(panels)
for row in board:
    print(''.join(row))