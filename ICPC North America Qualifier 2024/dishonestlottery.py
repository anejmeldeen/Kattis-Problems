n = int(input())

counts = {}

for _ in range(10 * n):
    arr = list(map(int, input().split()))
    for ele in arr:
        counts[ele] = counts.get(ele, 0) + 1

sol = []
for key in counts:
    if counts[key] > 2 * n:
        sol.append(key)

sol.sort()

if len(sol) == 0:
    print(-1)
else:
    print(' '.join(list(map(str, sol))))