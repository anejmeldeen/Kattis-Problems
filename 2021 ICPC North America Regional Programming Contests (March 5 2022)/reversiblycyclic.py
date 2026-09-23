s = input()
if s[::-1] in s + s:
    print(1)
else:
    print(0)