cards = []
for _ in range(4):
    cards += input().split()

stack = []
for card in cards:
    stack.append(card)
    found = True
    while found:
        found = False
        choice = 0
        idx = -1
        for i in range(3, len(stack)):
            if stack[i][0] == stack[i - 3][0]:
                choice = 2
                idx = i
                found = True
            if stack[i][1] == stack[i - 3][1]:
                if choice <= 1:
                    choice = 1
                    idx = i
                found = True
        if choice == 0:
            continue
        elif choice == 1:
            stack.pop(idx)
            stack.pop(idx - 3)
        elif choice == 2:
            stack.pop(idx)
            stack.pop(idx - 1)
            stack.pop(idx - 2)
            stack.pop(idx - 3)

print(len(stack), end=" ")
print(' '.join(stack))