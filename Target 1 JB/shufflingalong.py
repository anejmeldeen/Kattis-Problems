num, in_out = input().split()
num = int(num)

arr = [i for i in range(1, num + 1)]
og = arr.copy()

count = 0
while True:
    if in_out == "out" and num % 2 == 1:
        break_point = num // 2 + 1
    else:
        break_point = num // 2

    half1 = arr[:break_point]
    half2 = arr[break_point:]
    new_arr = []
    count += 1

    if in_out == "out":
        for i in range(num // 2):
            new_arr.append(half1[i])
            new_arr.append(half2[i])
        if num % 2 == 1:
            new_arr.append(half1[-1])
    else:
        for i in range(num // 2):
            new_arr.append(half2[i])
            new_arr.append(half1[i])
        if num % 2 == 1:
            new_arr.append(half2[-1])

    arr = new_arr
    if arr == og:
        break

print(count)