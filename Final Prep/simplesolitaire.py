cards = []
for _ in range(4):
    cards += input().split()

stack = []
for card in cards:
    stack.append(card)

    while True:
        move = 0
        idx = -1
        for i in range(len(stack) - 3):
            if stack[i][0] == stack[i + 3][0]:
                move = 2
                idx = i
            if stack[i][1] == stack[i + 3][1]:
                if move <= 1:
                    move = 1
                    idx = i

        if move == 0:
            break

        if move == 2:
            stack.pop(idx + 3)
            stack.pop(idx + 2)
            stack.pop(idx + 1)
            stack.pop(idx)
        else:
            stack.pop(idx + 3)
            stack.pop(idx)

print(len(stack), ' '.join(stack))