n, k = list(map(int, input().split()))
data = [0] * 25

data = []
for _ in range(n):
    start, end = list(map(int, input().split()))
    data.append((start, end))

sol = 0
for t in range(1, 25):
    count = 0
    for start, end in data:
        if start <= t - 1 and end >= t:
            count += 1
    if count >= k:
        sol += 1

print(sol)