x, y = list(map(int, input().split()))
n = int(input())

instructions = []
for _ in range(n):
    instructions.append(input())

done = False
for i in range(n):
    for instruction in ["Forward", "Left", "Right"]:
        if instructions[i] == instruction:
            continue

        direction = 0
        curr_x = curr_y = 0

        for j in range(n):
            move = instructions[j] if j != i else instruction

            if move == "Forward":
                if direction == 0:
                    curr_y += 1
                elif direction == 1:
                    curr_x += 1
                elif direction == 2:
                    curr_y -= 1
                else:
                    curr_x -= 1
            elif move == "Left":
                direction -= 1
                direction %= 4
            else:
                direction += 1
                direction %= 4

        if curr_x == x and curr_y == y:
            done = True
            print(f"{i + 1} {instruction}")
            break

    if done:
        break