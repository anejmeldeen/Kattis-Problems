n, m = list(map(int, input().split()))

graph = {}
forced = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    x, y = list(map(int, input().split()))

    if x < 0:
        x = -x
        forced[x] = y

    else:
        graph[x].append(y)

end = set()
def recurse(curr_node, seen, can_bug):
    global end

    new_seen = seen.copy()
    new_seen.add(curr_node)

    if curr_node not in forced:
        end.add(curr_node)
    elif forced[curr_node] not in seen:
        recurse(forced[curr_node], new_seen, can_bug)

    if can_bug:
        for conn in graph[curr_node]:
            if conn in seen:
                continue
            recurse(conn, seen, False)

recurse(1, set(), True)

print(len(end))