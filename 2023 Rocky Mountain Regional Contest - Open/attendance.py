n = int(input())
stack = []
for _ in range(n):
    word = input()
    if word == "Present!":
        stack.pop()
    else:
        stack.append(word)

if len(stack) == 0:
    print("No Absences")
for word in stack:
    print(word)