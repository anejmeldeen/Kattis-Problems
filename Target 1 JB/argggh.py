import math

n = int(input())
x, y = list(map(int, input().split()))

for _ in range(n - 1):
    direc, value = input().split()
    value = int(value)

    if direc == "N":
        y += value
    elif direc == "S":
        y -= value
    elif direc == "E":
        x += value
    elif direc == "W":
        x -= value
    else:
        shift = math.sqrt(value ** 2 / 2)
        if "N" in direc:
            y += shift
        if "S" in direc:
            y -= shift
        if "E" in direc:
            x += shift
        if "W" in direc:
            x -= shift

print(x, y)