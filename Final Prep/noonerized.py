equation = input().split()

num1 = equation[0]
num2 = equation[2]
num3 = equation[4]

op = equation[1]

for i in range(1, len(num1)):
    for j in range(1, len(num2)):
        fake1 = num2[:j] + num1[i:]
        fake2 = num1[:i] + num2[j:]
        if op == "+":
            if int(fake1) + int(fake2) == int(num3):
                print(f"{fake1} {op} {fake2} = {num3}")
                exit()
        else:
            if int(fake1) * int(fake2) == int(num3):
                print(f"{fake1} {op} {fake2} = {num3}")
                exit()

for i in range(1, len(num1)):
    for j in range(1, len(num3)):
        fake1 = num3[:j] + num1[i:]
        fake2 = num1[:i] + num3[j:]
        if op == "+":
            if int(fake1) + int(num2) == int(fake2):
                print(f"{fake1} {op} {num2} = {fake2}")
                exit()
        else:
            if int(fake1) * int(num2) == int(fake2):
                print(f"{fake1} {op} {num2} = {fake2}")
                exit()

for i in range(1, len(num3)):
    for j in range(1, len(num2)):
        fake1 = num2[:j] + num3[i:]
        fake2 = num3[:i] + num2[j:]
        if op == "+":
            if int(num1) + int(fake2) == int(fake1):
                print(f"{num1} {op} {fake2} = {fake1}")
                exit()
        else:
            if int(num1) * int(fake2) == int(fake1):
                print(f"{num1} {op} {fake2} = {fake1}")
                exit()