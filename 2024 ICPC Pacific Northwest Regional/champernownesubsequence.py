n = int(input())
number = input()

idx = 0
curr = 1
while True:
    str_curr = str(curr)
    for char in str_curr:
        if idx == n:
            break
        if number[idx] == char:
            idx += 1
    if idx == n:
        break
    curr += 1

print(curr)