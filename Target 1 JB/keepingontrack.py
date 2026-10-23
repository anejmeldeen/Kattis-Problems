import sys
sys.setrecursionlimit(int(1e9))

from collections import defaultdict
from functools import cache

n = int(input())

graph = defaultdict(list)
for _ in range(n):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

total_nodes = n + 1

blown_up = 0
recovery = 0

@cache
def get_size(node, prev):
    global blown_up, recovery

    total = 1
    sizes = []
    for conn in graph[node]:
        if conn != prev:
            sizes.append(get_size(conn, node))
            total += sizes[-1]

    sizes.append(total_nodes - 1 - sum(sizes))
    damage = 0
    damage_sum = sum(sizes)
    for size in sizes:
        damage += size * (damage_sum - size)
    damage //= 2

    if damage > blown_up:
        blown_up = damage
        if len(sizes) == 1:
            recov = 0
        else:
            maxi = max(sizes)
            sizes.remove(maxi)
            recov = maxi * max(sizes)
        recovery = damage - recov

    return total

get_size(0, -1)

print(blown_up, recovery)