digits = input()
sols = []
for char in digits:
    num = int(char)
    new = ""
    for _ in range(4):
        if num & 1:
            new = new + "*"
        else:
            new = new + "."
        num >>= 1
    sols.append(new)

for i in range(4):
    print(f"{sols[0][3 - i]} {sols[1][3 - i]}   {sols[2][3 - i]} {sols[3][3 - i]}")