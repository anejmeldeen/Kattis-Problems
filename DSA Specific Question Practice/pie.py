import math

t = int(input())

for _ in range(t):
    n, f = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    left = 0
    right = max(arr)
    iterations = 0
    while iterations < 100:
        iterations += 1
        mid = (left + right) / 2
        vol = math.pi * mid ** 2

        count = 0
        for i in range(n):
            count += (math.pi * arr[i] ** 2) // vol

        if count >= f + 1:
            left = mid
        else:
            right = mid
    print(math.pi * right ** 2)