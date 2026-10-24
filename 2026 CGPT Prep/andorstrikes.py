from collections import defaultdict

n, t = input().split()
n = int(n)

levels = []
for _ in range(n):
    levels.append(input().split())

idx = defaultdict(int)

def recurse(level):
    val = levels[level][idx[level]]
    idx[level] += 1

    if val == "T":
        return (True, 1)
    elif val == "F":
        return (False, 1)

    val = int(val)
    if level % 2 == 0:
        is_and = (t == "A")
    else:
        is_and = (t != "A")

    children = []
    for _ in range(val):
        children.append(recurse(level + 1))

    if is_and:
        false_nodes = 0
        false_nodes_cost = 0
        min_cost = float('inf')
        for child in children:
            if child[0]:
                min_cost = min(min_cost, child[1])
            else:
                false_nodes += 1
                false_nodes_cost += child[1]
        if false_nodes == 0:
            return (True, min_cost)
        return (False, false_nodes_cost)
    else:
        true_nodes = 0
        true_nodes_cost = 0
        min_cost = float('inf')
        for child in children:
            if child[0]:
                true_nodes += 1
                true_nodes_cost += child[1]
            else:
                min_cost = min(min_cost, child[1])
        if true_nodes == 0:
            return (False, min_cost)
        return (True, true_nodes_cost)

print(recurse(0)[1])