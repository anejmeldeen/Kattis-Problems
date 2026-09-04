n, t, a, b = list(map(int, input().split()))
arr = list(map(int, input().split()))

count = 0
direc = 1 if a <= arr[0] else 0
next = arr[0]
for i in range(t - 1):
    curr = arr[i]
    next = arr[i + 1]
    if curr == next:
        continue
    if curr < next:
        if direc == 0:
            direc = 1
            count += 1
    else:
        if direc == 1:
            direc = 0
            count += 1
if direc == 1 and next >= b:
    count += 1
if direc == 0 and next < b:
    count += 1

print(count)