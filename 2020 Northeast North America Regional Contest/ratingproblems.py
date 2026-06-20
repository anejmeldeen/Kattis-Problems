n, k = list(map(int, input().split()))

total = 0
for _ in range(k):
    total += int(input())

cpy = total

total += 3 * (n - k)
new_total = cpy + -3 * (n - k)

print(new_total / n, total / n)