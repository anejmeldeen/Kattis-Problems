n, k = list(map(int, input().split()))

problems = []
for _ in range(n):
    data = input().split()
    problems.append(data[1:])

count = 0
for i in range(1 << n):
    counts = {}
    impossible = False
    idx = 0
    ones = 0
    while i > 0:
        if i & 1:
            include = problems[idx]
            for tag in include:
                counts[tag] = counts.get(tag, 0) + 1
                if counts[tag] > k // 2:
                    impossible = True
            ones += 1
        i >>= 1
        idx += 1
    if not impossible and ones == k:
        count += 1

print(count)