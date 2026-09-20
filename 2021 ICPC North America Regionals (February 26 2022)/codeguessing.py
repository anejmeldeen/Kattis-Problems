x, y = list(map(int, input().split()))
order = input()

x = min(x, y)
y = max(x, y)

nums = [-1] * 4
first = True
for i in range(4):
    if order[i] == "A":
        if first:
            nums[i] = x
            first = False
        else:
            nums[i] = y

sols = 0
sol_x = sol_y = -1
for new_x in range(1, 10):
    for new_y in range(new_x + 1, 10):
        if new_x in [x, y] or new_y in [x, y]:
            continue

        new_nums = nums.copy()
        first = True
        for i in range(4):
            if order[i] == "B":
                if first:
                    new_nums[i] = new_x
                    first = False
                else:
                    new_nums[i] = new_y

        if new_nums == sorted(new_nums):
            sols += 1
            sol_x = new_x
            sol_y = new_y

if sols == 1:
    print(sol_x, sol_y)
else:
    print(-1)