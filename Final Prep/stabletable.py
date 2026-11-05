from collections import defaultdict, deque

r, c = list(map(int, input().split()))

graph = defaultdict(set)
end = 10000

board = []
for i in range(r):
    board.append(list(map(int, input().split())))

locs = set([end])
for i in range(r - 1):
    for j in range(c):
        locs.add(board[i][j])
        locs.add(board[i + 1][j])
        graph[board[i][j]].add(board[i + 1][j])

tops = set()
for j in range(c):
    graph[board[-1][j]].add(end)
    tops.add(board[0][j])

tops = list(tops)
top1 = tops.pop()
if len(tops) == 0:
    top2 = end
else:
    top2 = tops.pop()

def dist_finder(loc, mappy, cost, graph):
    queue = deque([(loc, cost)])
    while queue:
        loc, cost = queue.popleft()
        if loc in mappy:
            continue
        mappy[loc] = cost

        for conn in graph[loc]:
            if conn not in mappy:
                queue.append((conn, cost + 1))

rev_graph = defaultdict(set)
for key in graph:
    for item in graph[key]:
        rev_graph[item].add(key)

top1_dists = {}
top2_dists = {}
end_dists = {}
dist_finder(top1, top1_dists, 0, graph)
dist_finder(top2, top2_dists, 0, graph)
dist_finder(end, end_dists, 0, rev_graph)

best = top1_dists[end] + top2_dists[end]
for item in locs:
    best = min(best, top1_dists.get(item, float('inf')) + top2_dists.get(item, float('inf')) + end_dists[item])

print(best)