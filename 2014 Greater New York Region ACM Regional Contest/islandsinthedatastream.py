P = int(input())
for _ in range(P):
    arr = list(map(int, input().split()))
    K = arr[0]

    arr = arr[1:]

    count = 0
    for i in range(1, 11):
        mini = arr[i]
        for j in range(i, 11):
            mini = min(mini, arr[j])
            if mini > arr[i - 1] and mini > arr[j + 1]:
                count += 1
    
    print(K, count)