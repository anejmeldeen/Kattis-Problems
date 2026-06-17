P = int(input())
for _ in range(P):
    k, n = list(map(int, input().split()))

    last = 1
    arr = [0] * 79

    for _ in range(n):
        high = 0
        while arr[high] != 0:
            high += 1
        high -= 1

        for i in range(high + 1):
            arr[i] -= 1
        arr[high + 1] = high + 2
        last = max(last, high + 2)

    print(k, last)
    
    arr = arr[:last]
    idx = 0

    while idx < len(arr):
        print(' '.join(list(map(str, arr[idx:idx + 10]))))
        idx += 10