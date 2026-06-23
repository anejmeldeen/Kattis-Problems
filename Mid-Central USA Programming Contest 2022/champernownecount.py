n, k = list(map(int, input().split()))

num = 0
count = 0
for curr in range(1, n + 1):
    num *= 10 ** len(str(curr))
    num += curr
    num %= k

    if num == 0:
        count += 1

print(count)