dept1 = input()
dept2 = input()

def solve(dept):
    dicty = {}
    stack = []
    curr = ""
    for char in dept:
        if char not in "() ":
            curr += char
        elif char in "()" and curr != "":
            curr_int = int(curr)
            if stack:
                dicty[curr_int] = stack[-1]
            else:
                dicty[curr_int] = -1

            stack.append(curr_int)
            curr = ""
        if char == ")":
            stack.pop()
    if curr != "":
        dicty[curr] = -1

    return dicty

dict1 = solve(dept1)
dict2 = solve(dept2)

equivalent = True
for num in dict1:
    if num not in dict2 or dict1[num] != dict2[num]:
        equivalent = False
        break
for num in dict2:
    if num not in dict1 or dict1[num] != dict2[num]:
        equivalent = False
        break

if equivalent:
    print("Yes")
else:
    print("No")