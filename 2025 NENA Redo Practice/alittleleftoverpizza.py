import math

n = int(input())
s = m = l = 0

for _ in range(n):
    tag, num = input().split()
    if tag == "S":
        s += int(num)
    elif tag == "M":
        m += int(num)
    else:
        l += int(num)

print(math.ceil(s / 6) + math.ceil(m / 8) + math.ceil(l / 12))