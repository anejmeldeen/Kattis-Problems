first_code = input()
second_code = input()

ways = 1
for i in range(len(first_code)):
    if first_code[i] != second_code[i]:
        ways *= 2

print(ways)