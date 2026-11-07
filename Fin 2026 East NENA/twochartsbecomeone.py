import sys
sys.setrecursionlimit(int(1e5))

tree1 = input()
tree2 = input()
tree1 = tree1.replace(" ", "")
tree2 = tree2.replace(" ", "")

class Node:
    def __init__(self, val):
        self.val = val
        self.graph = {}

def evaluate_tree(tree):
    if "(" not in tree:
        num = int(tree)
        return Node(int(num))

    idx = tree.index("(")
    num = tree[:idx]
    equation = tree[idx:]

    node = Node(int(num))
    count = 0
    left = 0
    for right, char in enumerate(equation):
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count == 0:
                new_node = evaluate_tree(equation[left + 1:right])
                node.graph[new_node.val] = new_node
                left = right + 1

    return node

def same_tree(tree1, tree2):
    if tree1.val != tree2.val:
        return False
    for child in tree1.graph:
        if child not in tree2.graph:
            return False
    for child in tree2.graph:
        if child not in tree1.graph:
            return False
    works = True
    for child in tree1.graph:
        works = works and same_tree(tree1.graph[child], tree2.graph[child])
    return works

tree1 = evaluate_tree(tree1)
tree2 = evaluate_tree(tree2)

if same_tree(tree1, tree2):
    print("Yes")
else:
    print("No")