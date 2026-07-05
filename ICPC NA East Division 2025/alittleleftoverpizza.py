import math

n = int(input())
small = 0
med = 0
large = 0
for _ in range(n):
    data = input().split()
    count = int(data[1])
    if data[0] == "S":
        small += count
    elif data[0] == "M":
        med += count
    else:
        large += count

print(math.ceil(small / 6) + math.ceil(med / 8) + math.ceil(large / 12))