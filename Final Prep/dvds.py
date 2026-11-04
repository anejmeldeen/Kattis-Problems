t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i, ele in enumerate(arr):
        if ele - 1 != i - count:
            count += 1
    print(count)