n = int(input())
arr = list(map(int, input().split()))

stack = []
for num in arr:
    while stack and stack[-1] == num:
        stack.pop()
        num *= 2
    stack.append(num)

while len(stack) > 1:
    smallest = float('inf')
    smallest_loc = -1
    for i, num in enumerate(stack):
        if num < smallest:
            smallest = num
            smallest_loc = i

    stack = stack[:smallest_loc] + stack[smallest_loc + 1:]
    new_stack = []

    for num in stack:
        while new_stack and new_stack[-1] == num:
            new_stack.pop()
            num *= 2
        new_stack.append(num)

    stack = new_stack

print(stack[0])