from collections import deque

n, m = list(map(int, input().split()))

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

top = set(board[0])
bottom = set(board[-1])

connections = {}
for i in range(n - 1):
    for j in range(m):
        if board[i][j] not in connections:
            connections[board[i][j]] = set()

        connections[board[i][j]].add(board[i + 1][j])

up_connections = {}
for i in range(n - 1):
    for j in range(m):
        if board[i + 1][j] not in up_connections:
            up_connections[board[i + 1][j]] = set()

        up_connections[board[i + 1][j]].add(board[i][j])

def bfs(start_pieces, graph):
    dists = {}
    queue = deque()
    for piece in start_pieces:
        dists[piece] = 1
        queue.append(piece)

    while queue:
        curr = queue.popleft()
        if curr in graph:
            for conn in graph[curr]:
                if conn not in dists:
                    queue.append(conn)
                dists[conn] = min(dists.get(conn, float('inf')), dists[curr] + 1)

    return dists

piece_dicts = []
for piece in top:
    piece_dicts.append(bfs([piece], connections))

dist_to_bot = bfs(bottom, up_connections)

best = 0
for start in top:
    best += dist_to_bot[start]

if len(piece_dicts) > 1:
    piece_dict_1 = piece_dicts[0]
    piece_dict_2 = piece_dicts[1]

    for piece in piece_dict_1:
        if piece in piece_dict_2:
            best = min(best, dist_to_bot[piece] + piece_dict_1[piece] + piece_dict_2[piece] - 2)

print(best)