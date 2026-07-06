equation = input().split()

num1 = equation[0]
oper = equation[1]
num2 = equation[2]
num3 = equation[4]

# first and second
for i in range(1, len(num1)):
    for j in range(1, len(num2)):
        new_num1 = int(num2[:j] + num1[i:])
        new_num2 = int(num1[:i] + num2[j:])
        new_num3 = int(num3)
        if oper == "*":
            if new_num1 * new_num2 == new_num3:
                print(f"{new_num1} {oper} {new_num2} = {new_num3}")
        else:
            if new_num1 + new_num2 == new_num3:
                print(f"{new_num1} {oper} {new_num2} = {new_num3}")

# second and third
for i in range(1, len(num2)):
    for j in range(1, len(num3)):
        new_num1 = int(num1)
        new_num2 = int(num3[:j] + num2[i:])
        new_num3 = int(num2[:i] + num3[j:])
        if oper == "*":
            if new_num1 * new_num2 == new_num3:
                print(f"{new_num1} {oper} {new_num2} = {new_num3}")
        else:
            if new_num1 + new_num2 == new_num3:
                print(f"{new_num1} {oper} {new_num2} = {new_num3}")

# first and third
for i in range(1, len(num1)):
    for j in range(1, len(num3)):
        new_num1 = int(num3[:j] + num1[i:])
        new_num2 = int(num2)
        new_num3 = int(num1[:i] + num3[j:])
        if oper == "*":
            if new_num1 * new_num2 == new_num3:
                print(f"{new_num1} {oper} {new_num2} = {new_num3}")
        else:
            if new_num1 + new_num2 == new_num3:
                print(f"{new_num1} {oper} {new_num2} = {new_num3}")