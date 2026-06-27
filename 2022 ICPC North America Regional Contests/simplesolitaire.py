cards = []
for _ in range(4):
    arr = input().split()
    cards += arr

stack = []
for card in cards:
    stack.append(card)
    change = True
    while change:
        change = False
        found_small = False
        small_loc = -1
        for i in range(len(stack) - 1, 2, -1):
            card1 = stack[i - 3]
            card2 = stack[i]
            num1 = card1[0]
            suit1 = card1[1]
            num2 = card2[0]
            suit2 = card2[1]

            if num1 == num2:
                change = True
                stack = stack[:i - 3] + stack[i + 1:]
                found_small = False
                break

            if suit1 == suit2 and small_loc == -1:
                found_small = True
                small_loc = i
                change = True

        if found_small:
            stack = stack[:small_loc - 3] + stack[small_loc - 2:small_loc] + stack[small_loc + 1:]

print(len(stack), end=" ")
print(' '.join(stack))