n, k = list(map(int, input().split()))

prev_row = []
count = 0
for j in range(n + 1):
    row = [1 % k]
    for i in range(len(prev_row) - 1):
        row.append((prev_row[i] + prev_row[i + 1]) % k)
    if j > 0:
        row.append(1 % k)

    for item in row:
        if item % k == 0:
            count += 1

    prev_row = row

print(count)