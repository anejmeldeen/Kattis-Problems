string = input()

a, b, c = 0, 0, 0
maxi = 0
for char in string:
    if char == "A":
        a += 1
    if char == "B":
        b += 1
    if char == "C":
        c += 1

    mini = min(a, b, c)
    a -= mini
    b -= mini
    c -= mini

    maxi = max(maxi, a, b, c)

print(maxi)