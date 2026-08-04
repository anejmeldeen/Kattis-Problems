string = input()
seen = set()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    seen = set()
    found = False
    for char in string:
        if char == letter:
            if found:
                seen = set()
            found = True
        elif found:
            if char not in seen:
                seen.add(char)
                total += 1

print(total)