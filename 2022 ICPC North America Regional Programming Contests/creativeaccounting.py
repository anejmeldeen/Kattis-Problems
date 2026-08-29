n, l, h = list(map(int, input().split()))
profits = []

for _ in range(n):
    profits.append(int(input()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + profits[i - 1]

mini = float('inf')
maxi = -float('inf')
for x in range(l, h + 1):
    for start in range(1, x + 1):
        works = True
        count = 0
        if prefix[start] > 0:
            count += 1
        for k in range(start + 1, n + 1, x):
            right = min(n, k + x - 1)
            left = k - 1
            if prefix[right] - prefix[left] > 0:
                count += 1

        mini = min(mini, count)
        maxi = max(maxi, count)

print(mini, maxi)