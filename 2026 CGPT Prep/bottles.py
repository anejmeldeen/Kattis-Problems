import sys

n = int(input())

powwy = 1
friends = 0
while powwy < n:
    powwy *= 2
    friends += 1

print(friends)
sys.stdout.flush()

friend_arr = []

for bit_shift in range(friends):
    mask = 1 << bit_shift

    arr = []
    for bottle in range(1, n + 1):
        if bottle & mask:
            arr.append(bottle)

    friend_arr.append(set(arr))
    print(len(arr), ' '.join(list(map(str, arr))))
    sys.stdout.flush()

res = input()
overall_set = {i for i in range(1, n + 1)}
for i in range(len(res)):
    setty = friend_arr[i]
    if res[i] == "1":
        overall_set &= setty
    else:
        setty = {i for i in range(1, n + 1) if i not in setty}
        overall_set &= setty

print(overall_set.pop())
sys.stdout.flush()