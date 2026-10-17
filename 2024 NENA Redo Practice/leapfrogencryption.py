t, k = input().split()
string = input()

key = []
for char in k:
    key.append(ord(char) - ord('a') + 2)

alpha_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

real_string = []
for char in string:
    if char in alpha_set:
        real_string.append(char.lower())
string = ''.join(real_string)

arr_locs = [-1] * len(string)

right = True
idx = 0
for every_n in key:
    if right:
        low = 0
        high = len(string)
        diff = 1
    else:
        low = len(string) - 1
        high = -1
        diff = -1

    count = 0

    for i in range(low, high, diff):
        if arr_locs[i] != -1:
            continue
        count += 1
        if count == every_n:
            arr_locs[i] = idx
            idx += 1
            count = 0
    right = not right

if right:
    low = 0
    high = len(string)
    diff = 1
else:
    low = len(string) - 1
    high = -1
    diff = -1
for i in range(low, high, diff):
    if arr_locs[i] == -1:
        arr_locs[i] = idx
        idx += 1

if t == "E":
    sol = [0] * len(string)
    for i, idx in enumerate(arr_locs):
        sol[i] = string[idx]
    print(''.join(sol))
else:
    sol = [0] * len(string)
    for idx, i in enumerate(arr_locs):
        sol[i] = string[idx]
    print(''.join(sol))