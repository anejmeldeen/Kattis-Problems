from collections import deque

n = int(input())
words = []
chars = set()
for _ in range(n):
    x = input()
    words.append(x)
    setty = set(x)
    chars = chars | setty

adj = {x: [] for x in chars}
in_degree = {x: 0 for x in chars}
for i in range(n - 1):
    curr, next = words[i], words[i + 1]
    a = b = - 1
    l = min(len(curr), len(next))
    for j in range(l):
        if curr[j] != next[j]:
            a, b = curr[j], next[j]
            break
    if a != -1:
        if a not in adj:
            adj[a] = []
        adj[a].append(b)
        in_degree[b] += 1

queue = deque([x for x in in_degree if in_degree[x] == 0])
ans = []
ambig = False
while queue:
    if len(queue) > 1:
        ambig = True
    node = queue.popleft()
    ans.append(node)

    for out in adj[node]:
        in_degree[out] -= 1
        if in_degree[out] == 0:
            queue.append(out)

if len(ans) < len(chars):
    print("IMPOSSIBLE")
elif ambig:
    print("AMBIGUOUS")
else:
    print(''.join(ans))