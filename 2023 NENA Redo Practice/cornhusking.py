arr = list(map(int, input().split()))

summ = 0
for i in range(0, 10, 2):
    summ += arr[i] * arr[i + 1]
summ //= 5

first, second = list(map(int, input().split()))

print(int(summ * first // second))