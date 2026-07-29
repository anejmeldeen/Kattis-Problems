n = int(input())
bin_str = input()

count = 0
sol = 0
for char in bin_str:
    if char == '1':
        sol += 1
        count = 2
    else:
        if count > 0:
            sol += 1
        count -= 1

print(sol)