string = input()

def rotate(char, rotate_val):
    rotate_val %= 26
    char_val = ord(char)
    char_val += rotate_val
    if char_val > ord("Z"):
        char_val %= (ord("Z") + 1)
        char_val += ord("A")
    return chr(char_val)

def modify(string):
    total = 0
    for char in string:
        total += ord(char) - ord("A")

    res = []
    for char in string:
        res.append(rotate(char, total))
    return ''.join(res)

first_half = string[:len(string) // 2]
second_half = string[len(string) // 2:]

first_half = modify(first_half)
second_half = modify(second_half)

sol = []
for i in range(len(first_half)):
    sol.append(rotate(first_half[i], ord(second_half[i]) - ord("A")))
print(''.join(sol))