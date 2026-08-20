n = int(input())
arr = list(map(int, input().split()))

maxis = [float('-inf')] * (n + 1)
minis = [float('inf')] * (n + 1)

for i in range(1, n + 1):
    maxis[i] = max(arr[i - 1], maxis[i - 1])
for i in range(n - 1, -1, -1):
    minis[i] = min(arr[i], minis[i + 1])

count = 0
for i in range(n):
    if maxis[i] < arr[i] and arr[i] < minis[i + 1]:
        count += 1

print(count)