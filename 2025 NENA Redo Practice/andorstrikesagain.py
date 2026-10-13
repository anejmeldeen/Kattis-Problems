from collections import defaultdict

class Node:
    def __init__(self, truth_val=None, swap_cost=float('inf')):
        self.truth_val = truth_val
        self.swap_cost = swap_cost
        
n, t = input().split()
n = int(n)

levels = []
for _ in range(n):
    levels.append(input().split())

level_idx = defaultdict(int)
def construct_root(level):
    is_and = True
    if level % 2 == 0 and t == "O":
        is_and = False
    elif level % 2 == 1 and t == "A":
        is_and = False

    idx = level_idx[level]
    level_idx[level] += 1
    val = levels[level][idx]
    if val == "T":
        return Node(True, 1)
    elif val == "F":
        return Node(False, 1)
    val = int(val)

    curr_node = Node()
    evaluation = True if is_and else False
    total_true_cost = total_false_cost = 0
    min_cost = float('inf')
    for _ in range(val):
        child_node = construct_root(level + 1)
        if is_and:
            evaluation = evaluation and child_node.truth_val
        else:
            evaluation = evaluation or child_node.truth_val

        if child_node.truth_val:
            total_true_cost += child_node.swap_cost
        else:
            total_false_cost += child_node.swap_cost

        min_cost = min(min_cost, child_node.swap_cost)

    curr_node.truth_val = evaluation
    if evaluation and is_and:
        curr_node.swap_cost = min_cost
    elif not evaluation and is_and:
        curr_node.swap_cost = total_false_cost
    elif evaluation and not is_and:
        curr_node.swap_cost = total_true_cost
    else:
        curr_node.swap_cost = min_cost
        
    return curr_node

root = construct_root(0)
print(root.swap_cost)