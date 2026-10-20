n = int(input())
arr = list(map(int, input().split()))
arr = [(arr[i], i) for i in range(n)]

idx = 0
for _ in range(n - 1):
    count = arr[idx][0]
    idx = (idx + count - 1) % len(arr)
    arr = arr[:idx] + arr[idx + 1:]
    idx %= len(arr)

print(arr[0][1] + 1)