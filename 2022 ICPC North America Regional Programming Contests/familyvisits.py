n, d = list(map(int, input().split()))
increment, decrement = [], []

for _ in range(n):
    a, b = list(map(int, input().split()))
    increment.append(a)
    decrement.append(b)

days = []
for _ in range(d):
    days.append(int(input()))

intervals = []
left = 1
for right in days:
    intervals.append((left, right))
    left = right + 1

solution = 0
for start, end in intervals:
    adders = increment[start - 1:end]
    removers = decrement[start - 1:end]
    n = len(adders)

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n):
        new_dp = [x + adders[i] for x in dp]
        for j in range(n, 0, -1):
            new_dp[j] = min(new_dp[j], max(new_dp[j - 1] - removers[i], 0))
        dp = new_dp
    found = False
    for k in range(n + 1):
        if dp[k] == 0:
            solution += k
            found = True
            break

    if not found:
        print(-1)
        exit()

print(solution)