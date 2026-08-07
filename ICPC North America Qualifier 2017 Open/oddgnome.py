t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    arr = data[1:]

    prev = arr[0]
    king = -1
    for i in range(1, n):
        if arr[i] != prev + 1:
            king = i + 1
            break
        prev = arr[i]

    print(king)