import math

arr = list(map(int, list(input())))
n = len(arr)
maxi = [arr[0]] * n
maxi_rev = [arr[-1]] * n

def count_under(arr, num):
    count = 0
    curr = 0
    for ele in arr:
        if ele > num:
            count += curr * (curr + 1) // 2
            curr = 0
        else:
            curr += 1
    count += curr * (curr + 1) // 2

    return count

count = 0
total = n * (n + 1) // 2
for num in set(arr):
    count += num * (count_under(arr, num) - count_under(arr, num - 1))

inty = count // total
rem = count % total

geecd = math.gcd(rem, total)

rem //= geecd
total //= geecd


if rem == 0:
    print(inty)
elif inty == 0:
    print(f"{rem}/{total}")
else:
    print(f"{inty} {rem}/{total}")