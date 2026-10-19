t = int(input())

for _ in range(t):
    string = input()

    valid = True
    if string[-1] == "-" or string[0] == "-":
        valid = False
    if string.count("-") > 3:
        valid = False
    if string.count("-") == 3 and string[-2] != "-":
        valid = False

    for i in range(len(string) - 1):
        if string[i] == string[i + 1] and string[i] == "-":
            valid = False

    digits = []
    for i, char in enumerate(string):
        if char != "-":
            if char == "X":
                if i != len(string) - 1:
                    valid = False
                char = 10
            digits.append(int(char))

    if len(digits) != 10 or not valid:
        print("invalid")
        continue

    summ = 0
    for i in range(10):
        summ += (10 - i) * digits[i]
    if summ % 11 != 0:
        valid = False

    if valid:
        summ = 38
        for i in range(9):
            if i % 2 == 0:
                mult = 3
            else:
                mult = 1
            summ += mult * digits[i]

        diff = summ % 10
        checksum = (-diff) % 10
        
        print("978-" + string[:-1] + str(checksum))
    else:
        print("invalid")