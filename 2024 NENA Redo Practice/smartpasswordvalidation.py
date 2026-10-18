password = input()
n = int(input())

chars = """`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?"""

left_normal = "`123456qwertasdfgzxcvb~!@#$%^QWERTASDFGZXCVB"
left_shift =  "1234567wertysdfghxcvbn!@#$%^&WERTYSDFGHXCVBN"

right_normal = "7890-=yuiop[]\\hjkl;'nm,./&*()_+YUIOP{}|HJKL:\"NM<>?"
right_shift =  "67890-tyuiop[]ghjkl;bnm,.^&*()_TYUIOP{}GHJKL:BNM<>"

caps_normal = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
caps_shift = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

left_to_shift = {left_normal[i]:left_shift[i] for i in range(len(left_normal))}
right_to_shift = {right_normal[i]:right_shift[i] for i in range(len(right_normal))}
caps_to_shift = {caps_normal[i]:caps_shift[i] for i in range(len(caps_normal))}

minus_char = set()
for i in range(len(password)):
    new_password = password[:i] + password[i + 1:]
    minus_char.add(new_password)

extra_char = set()
for i in range(len(password) + 1):
    first = password[:i]
    second = password[i:]
    for char in chars:
        extra_char.add(first + char + second)

left_shift = set()
left_shifted = []
for char in password:
    if char in left_normal:
        left_shifted.append(left_to_shift[char])
    else:
        left_shifted.append(char)
left_shift.add(''.join(left_shifted))

right_shift = set()
right_shifted = []
for char in password:
    if char in right_normal:
        right_shifted.append(right_to_shift[char])
    else:
        right_shifted.append(char)
right_shift.add(''.join(right_shifted))

allowed = left_shift | right_shift | extra_char | minus_char | set([password])

new_allowed = set()
for password in allowed:
    new_allowed.add(password)
    shifted = []
    for char in password:
        if char not in caps_to_shift:
            shifted.append(char)
        else:
            shifted.append(caps_to_shift[char])
    new_allowed.add(''.join(shifted))

for _ in range(n):
    trial = input()
    if trial in new_allowed:
        print("YES")
    else:
        print("NO")