n = int(input())
confusing = {'B':8, 'G':'C', 'I':1, 'O':0, 'Q':0, 'S':5, 'U':'V', 'Y':'V', 'Z':2}
values = {char : i for i, char in enumerate("0123456789ACDEFHJKLMNPRTVWX")}

for _ in range(n):
    k, code = input().split()
    new_code = ""
    for char in code:
        if char in confusing:
            new_code += confusing[char]
        else:
            new_code += char
    code = new_code

    check_digit = 2*values[code[0]] + 4*values[code[1]] + 5*values[code[2]] + 7*values[code[3]] + 8*values[code[4]] + 10*values[code[5]] + 11*values[code[6]] + 13*values[code[7]]
    check_digit %= 27

    og_check = values[code[8]]

    if og_check != check_digit:
        print(k, "invalid")
    else:
        total = 0
        mult = 1
        idx = 7
        while idx >= 0:
            total += values[code[idx]] * mult
            mult *= 27
            idx -= 1
        print(k, total)