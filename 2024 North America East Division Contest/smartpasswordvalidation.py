password = input()
n = int(input())

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"

flip_cap = {}
for i in range(26):
    flip_cap[LOWER[i]] = UPPER[i]
    flip_cap[UPPER[i]] = LOWER[i]
characters = UPPER + LOWER + "`1234567890-=~!@#$%^&*()_+[]\\|\\{\\};:'\",./<>?"
characters = UPPER + LOWER + "`1234567890-=~!@#$%^&*()_+[]\\|\\{\\};:'\",./<>?"
characters = set(characters)

left = """`123456~!@#$%^qwertQWERTasdfgASDFGzxcvbZXCVB"""
left_shift = """1234567!@#$%^&wertyWERTYsdfghSDFGHxcvbnXCVBN"""
right = """7890-=&*()_+yuiop[]\\YUIOP{}|hjkl;'HJKL:"nm,./NM<>?"""
right_shift = """67890-^&*()_tyuiop[]TYUIOP{}ghjkl;GHJKL:bnm,.BNM<>"""

left_shifter = {}
right_shifter = {}

for i in range(len(left)):
    left_shifter[left[i]] = left_shift[i]
for i in range(len(right)):
    right_shifter[right[i]] = right_shift[i]

passwords = set([password])
extras = set()
minuses = set()

# extras and minuses
for pos in range(len(password) + 1):
    for char in characters:
        extras.add(password[:pos] + char + password[pos:])
    if pos < len(password):
        for char in characters:
            minuses.add(password[:pos] + password[pos + 1:])

# right and left shift
rights = set()
lefts = set()
for password in passwords:
    new_left = ""
    for char in password:
        if char in left_shifter:
            new_left += left_shifter[char]
        else:
            new_left += char
    lefts.add(new_left)

    new_right = ""
    for char in password:
        if char in right_shifter:
            new_right += right_shifter[char]
        else:
            new_right += char
    rights.add(new_right)

for attempt in extras:
    passwords.add(attempt)
for attempt in minuses:
    passwords.add(attempt)
for attempt in rights:
    passwords.add(attempt)
for attempt in lefts:
    passwords.add(attempt)

# caps lock
caps_pass = set()
for password in passwords:
    new_pass = ""
    for char in password:
        if char in flip_cap:
            new_pass += flip_cap[char]
        else:
            new_pass += char
    caps_pass.add(new_pass)
for password in caps_pass:
    passwords.add(password)

for _ in range(n):
    attempt = input()
    if attempt in passwords:
        print("YES")
    else:
        print("NO")