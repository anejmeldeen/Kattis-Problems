n = int(input())
truth_values = input().split()

chars = input().split()
stack = []
for char in chars:
    if char in "+*-":
        if char == "+":
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val1 or val2)
        elif char == "*":
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val1 and val2)
        else:
            stack.append(not stack.pop())
    else:
        idx = ord(char) - ord('A')
        stack.append(True if truth_values[idx] == "T" else False)

print("T" if stack[0] else "F")