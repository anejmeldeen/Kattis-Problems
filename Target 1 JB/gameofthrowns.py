n, k = list(map(int, input().split()))

stack = []
data = input().split()
idx = 0

for _ in range(k):
    value = data[idx]
    if value == "undo":
        value = data[idx + 1]
        idx += 2
        for _ in range(int(value)):
            stack.pop()
    else:
        stack.append(int(value))
        idx += 1

summ = sum(stack)
print(summ % n)