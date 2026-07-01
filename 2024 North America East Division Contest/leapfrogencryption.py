t, k = input().split()
text = input()

d = []
for char in k:
    num = ord(char) - ord('a') + 2
    d.append(num)

new_text = ""
text = text.lower()
for char in text:
    if char in "abcdefghijklmnopqrstuvwxyz":
        new_text += char
text = new_text

def encrypt(text, key):
    sol = [-1] * len(text)
    right = True
    idx = 0

    for num in d:
        if right:
            lower = 0
            upper = len(text)
            change = 1
        else:
            lower = len(text) - 1
            upper = -1
            change = -1

        can_place = num

        for i in range(lower, upper, change):
            if idx == len(text):
                break
            if sol[i] == -1:
                can_place -= 1
                if can_place == 0:
                    sol[i] = idx
                    idx += 1
                    can_place = num
        
        right = not right

    if right:
        for i in range(len(text)):
            if sol[i] == -1:
                sol[i] = idx
                idx += 1
    else:
        for i in range(len(text) - 1, -1, -1):
            if sol[i] == -1:
                sol[i] = idx
                idx += 1

    return sol

order = encrypt(text, k)
if t == "E":
    sol = ["0"] * len(order)
    for i in range(len(order)):
        sol[i] = text[order[i]]
    print(''.join(sol))
else:
    sol = ["0"] * len(order)
    for i in range(len(order)):
        sol[order[i]] = text[i]
    print(''.join(sol))