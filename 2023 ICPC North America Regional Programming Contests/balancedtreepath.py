import sys
sys.setrecursionlimit(int(1e9))

n = int(input())
chars = input()

rev = {")": "(", "]": "[", "}": "{"}

graph = {}
for _ in range(n - 1):
    x, y = list(map(int, input().split()))

    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []

    graph[x].append(y)
    graph[y].append(x)


def dfs(curr_node, stack, parent):
    char = chars[curr_node - 1]
    curr_stack_len = len(stack)
    if stack and char in rev and rev[char] == stack[-1]:
        stack.pop()
    elif char in "])}":
        return 0
    else:
        stack.append(char)

    res = (len(stack) == 0)

    for conn in graph[curr_node]:
        if conn == parent:
            continue
        res += dfs(conn, stack, curr_node)

    if len(stack) > curr_stack_len:
        stack.pop()
    elif len(stack) < curr_stack_len:
        stack.append(rev[char])

    return res

sol = 0
for num in range(1, n + 1):
    sol += dfs(num, [], -1)

print(sol)