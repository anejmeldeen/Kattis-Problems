import sys
sys.set_int_max_str_digits(100000)

n, k = list(map(int, input().split()))
count = 0
add = 1
curr = ""
for x in range(n):
    curr += str(add)
    curr = str(int(curr) % k)
    if curr == "0":
        count += 1
    add += 1
print(count)