total = 0
string = input()

for char in string:
    total += ord(char)

print(chr(total // len(string)))