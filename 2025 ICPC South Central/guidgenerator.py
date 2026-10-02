import sys
sys.setrecursionlimit(int(1e9))

n = int(input())
string = input()

graph = {}
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    if a - 1 not in graph:
        graph[a - 1] = []
    if b - 1 not in graph:
        graph[b - 1] = []
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

class Trie():
    def __init__(self):
        self.children = {}

root = Trie()
count = 0

def recurse(num, root, prev):
    global count

    if string[num] not in root.children:
        root.children[string[num]] = Trie()
        count += 1
    root = root.children[string[num]]

    for conn in graph[num]:
        if conn == prev:
            continue
        recurse(conn, root, num)

for i in range(n):
    recurse(i, root, -1)

print(count)