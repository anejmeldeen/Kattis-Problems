n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr = [(x, i) for i, x in enumerate(arr)]
arr.sort(key=lambda x: x[0])

found = False
for i in range(len(arr) - 1):
    if abs(arr[i][1] - arr[i + 1][1]) == 1:
        found = True

if found:
    print("In at least partial order")
else:
    print("Totally out of order")