string = input()

works = (string[-1] == "O")
prev = "-1"
for char in string:
    if char not in "OE":
        works = False
    if char == "O" and prev == "O":
        works = False
    prev = char

powers = set()
for i in range(100):
    powers.add(2 ** i)

if not works:
    print("INVALID")
else:
    best = float('inf')
    for x in range(200):
        curr = 2 ** x
        impossible = False

        for i in range(len(string) - 1, -1, -1):
            if string[i] == "E":
                curr *= 2
            else:
                curr -= 1
                if curr % 3 != 0 or curr < 1:
                    impossible = True
                curr //= 3

            if curr in powers:
                impossible = True

        if not impossible:
            best = min(best, curr)
    print(best)