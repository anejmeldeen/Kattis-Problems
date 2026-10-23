from collections import defaultdict, deque

n, m = list(map(int, input().split()))

targets = input().split()

graph = defaultdict(list)
for _ in range(m):
    l1, l2, c = input().split()
    c = int(c)

    graph[l1].append((l2, c))
    graph[l2].append((l1, c))

lang_to_dist = {}
queue = deque([(0, "English")])
seen = set(["English"])

while queue:
    cost, lang = queue.popleft()
    lang_to_dist[lang] = cost

    for conn in graph[lang]:
        if conn[0] in seen:
            continue
        queue.append((cost + 1, conn[0]))
        seen.add(conn[0])

total = 0
for lang in targets:
    if lang not in lang_to_dist:
        print("Impossible")
        exit()

    dist = lang_to_dist[lang]
    prev_cost = float('inf')
    for conn_loc, conn_cost in graph[lang]:
        if lang_to_dist[conn_loc] != dist - 1:
            continue
        prev_cost = min(prev_cost, conn_cost)
    total += prev_cost
print(total)