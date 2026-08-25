n, w = list(map(int, input().split()))
incorrect = list(map(int, input().split()))

arr = [True] * n
for x in incorrect:
    arr[x - 1] = False

curr = -1
left = 0
c = []
w = []
for right in range(n):
    if arr[right] != curr and curr != -1:
        if left == right - 1:
            res = str(left + 1)
        else:
            res = str(left + 1) + "-" + str(right)
        if curr:
            c.append(res)
        else:
            w.append(res)
        left = right
        curr = arr[right]
    else:
        curr = arr[right]
if left == right:
    res = str(left + 1)
else:
    res = str(left + 1) + "-" + str(right + 1)
if curr:
    c.append(res)
else:
    w.append(res)

print("Errors: ", end="")
print(", ".join(w[:-1]), end="")
print(" and " + w[-1])

print("Correct: ", end="")
print(", ".join(c[:-1]), end="")
print(" and " + c[-1])