n, t = input().split()
n = int(n)
is_and = t == "A"

class Node:
    def __init__(self, num_children, is_and, evalu=False):
        self.num_children = num_children
        self.children = []
        self.is_and = is_and
        self.eval = evalu

root = Node(int(input()), is_and)
is_and = not is_and
prev_row = [root]
for _ in range(n - 1):
    data = input().split()
    idx = 0
    row = []
    for node in prev_row:
        for _ in range(node.num_children):
            item = data[idx]
            if item == "T":
                new_node = Node(0, is_and, True)
            elif item == "F":
                new_node = Node(0, is_and, False)
            else:
                new_node = Node(int(item), is_and)
            node.children.append(new_node)
            row.append(new_node)
            idx += 1
    prev_row = row
    is_and = not is_and

def evaluate(node):
    if node.num_children == 0:
        return (node.eval, 1)
    
    children_evals = []
    for child in node.children:
        children_evals.append(evaluate(child))

    if node.is_and:
        res = True
        for item in children_evals:
            res = res and item[0]
        
        if res == True:
            return (True, min([x[1] for x in children_evals]))
        else:
            total = 0
            for item in children_evals:
                if item[0] == False:
                    total += item[1]
            return (False, total)
    else:
        res = False
        for item in children_evals:
            res = res or item[0]
        
        if res == True:
            total = 0
            for item in children_evals:
                if item[0] == True:
                    total += item[1]
            return (True, total)
        else:
            return (False, min([x[1] for x in children_evals]))

print(evaluate(root)[1])