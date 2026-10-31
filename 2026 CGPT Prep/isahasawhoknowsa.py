import sys
from functools import cache
from collections import defaultdict

# sys.setrecursionlimit(int(1e9))

n, m = list(map(int, input().split()))

is_a = defaultdict(list)
has_a = defaultdict(list)

for _ in range(n):
    data = input().split()
    a = data[0]
    b = data[-1]

    if data[1] == "is-a":
        is_a[a].append(b)
    else:
        has_a[a].append(b)

def is_dfs(node, target, seen):
    if node in seen:
        return False
    seen.add(node)
    if node == target:
        return True

    works = False
    for conn in is_a[node]:
        if conn not in seen:
            works = works or is_dfs(conn, target, seen)
    return works

def has_dfs(node, target, seen, other_seen):
    if node in seen:
        return False
    seen.add(node)
    works = False
    for conn in is_a[node]:
        works = works or has_dfs(conn, target, seen, other_seen)
    for conn in has_a[node]:
        works = works or is_dfs(conn, target, other_seen) or has_dfs(conn, target, seen, other_seen)
    return works

@cache
def answer(query):
    a = query[0]
    b = query[-1]

    if query[1] == "is-a":
        works = (a == b) or is_dfs(a, b, set())
        val = "true" if works else "false"
        return val
    else:
        works = False
        works = has_dfs(a, b, set(), set())
        val = "true" if works else "false"
        return val

for i in range(m):
    query = tuple(input().split())
    val = answer(query)
    print(f"Query {i + 1}: {val}")