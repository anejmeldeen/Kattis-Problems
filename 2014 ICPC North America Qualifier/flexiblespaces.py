W, n = list(map(int, input().split()))
arr = [0]
in_arr = list(map(int, input().split()))

arr = arr + in_arr + [W]

lengths = set()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        lengths.add(arr[j] - arr[i])

lengths = list(lengths)
lengths.sort()

print(' '.join(list(map(str, lengths))))