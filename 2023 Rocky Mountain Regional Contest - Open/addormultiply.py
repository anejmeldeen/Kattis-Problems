n, m = list(map(int, input().split()))
equation = input()

MOD = 10**9 + 7

digits = []
operations = []

for char in equation:
    if char.isalnum():
        digits.append(int(char))
    else:
        operations.append(char)

operations.append("*")

orig_n = n
while n & (n - 1) != 0:
    n += 1
tree = [None] * (2 * n)
def merge_helper(left_state, right_state, operation):
    if operation == "+":
        is_pure = False
        new_left = left_state[1]
        new_right = right_state[1] if right_state[0] else right_state[2]
        new_mid = left_state[3] + right_state[3] + left_state[2] + (right_state[1] if not right_state[0] else 0)
    else:
        if left_state[0] and right_state[0]:
            is_pure = True
            new_left = left_state[1] * right_state[1]
            new_right = 0
            new_mid = 0
        elif left_state[0]:
            is_pure = False
            new_left = left_state[1] * right_state[1]
            new_right = right_state[2]
            new_mid = right_state[3]
        elif right_state[0]:
            is_pure = False
            new_left = left_state[1]
            new_right = left_state[2] * right_state[1]
            new_mid = left_state[3]
        else:
            is_pure = False
            new_left = left_state[1]
            new_right = right_state[2]
            new_mid = left_state[3] + right_state[3] + left_state[2] * right_state[1]
    return (is_pure, new_left % MOD, new_right % MOD, new_mid % MOD)
def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    operator = operations[left[0]]
    new_node, new_node_inv = -1, -1
    if operator == "+":
        new_node = merge_helper(left[1], right[1], "+")
        new_node_inv = merge_helper(left[2], right[2], "*")
    elif operator == "*":
        new_node = merge_helper(left[1], right[1], "*")
        new_node_inv = merge_helper(left[2], right[2], "+")
    return (right[0], new_node, new_node_inv)
def build(arr):
    for i in range(orig_n): 
        tree[n + i] = (i, (True, arr[i], 0, 0), (True, arr[i], 0, 0))
    for i in range(n - 1, 0, -1): 
        left_node = tree[i << 1]
        right_node = tree[i << 1 | 1]
        tree[i] = merge(left_node, right_node)
def update(p, value):
    p += n
    tree[p] = (tree[p][0], (True, value, 0, 0), (True, value, 0, 0))
    while p > 1:
        left_node = tree[min(p, p ^ 1)]
        right_node = tree[max(p, p ^ 1)]
        tree[p>>1] = merge(left_node, right_node)
        p >>= 1

build(digits)

use_second = False
def get_top():
    global use_second
    idx = 0
    while tree[idx] == None:
        idx += 1
    node = tree[idx][2 if use_second else 1]
    return (node[1] + node[2] + node[3]) % MOD

print(get_top())
for _ in range(m):
    query = input().split()
    if query[0] == "s":
        first = int(query[1]) - 1
        second = int(query[2]) - 1
        first_dig = digits[first]
        second_dig = digits[second]
        digits[first] = second_dig
        digits[second] = first_dig
        update(first, second_dig)
        update(second, first_dig)
    elif query[0] == "a":
        use_second = not use_second
    elif query[0] == "f":
        index = int(query[1]) - 1
        operations[index] = "+" if operations[index] == "*" else "*"
        update(index, digits[index])
    print(get_top())