n, s, k = list(map(int, input().split()))

locs = []
for _ in range(n):
    locs.append(int(input()))

locs.sort()

possible = True
for i in range(n - 1):
    if locs[i] + s > locs[i + 1]:
        possible = False

if not possible:
    print(-1)
else:
    intervals = []
    for loc in locs:
        intervals.append((loc - s / 2, loc + s / 2))

    low = 0
    high = n - 1
    while low < high:
        prev = (float('-inf'), float('-inf'))
        if low > 0:
            prev = intervals[low - 1]
        first = intervals[low]
        second = intervals[low + 1]
        dist = min(second[0] - first[1], first[0] - prev[1])
        add = min((k - s) / 2, dist)
        intervals[low] = (first[0] - add, first[1] + add)
        
        after = (float('inf'), float('inf'))
        if high < n - 1:
            after = intervals[high + 1]
        last = intervals[high] 
        prev = intervals[high - 1]
        dist = min(last[0] - prev[1], after[0] - last[1])
        add = min((k - s) / 2, dist)
        intervals[high] = (last[0] - add, last[1] + add)

        low += 1
        high -= 1

    if low == high:
        if n == 1:
            first = intervals[0]
            add = (k - s) / 2
            intervals[0] = (first[0] - add, first[1] + add)
        else:
            prev = intervals[low - 1]
            curr = intervals[low]
            nxt = intervals[low + 1]
            dist1 = curr[0] - prev[1]
            dist2 = nxt[0] - curr[1]
            min_dist = min(dist1, dist2)
            add = min((k - s) / 2, min_dist)
            intervals[low] = (curr[0] - add, curr[1] + add)

    total = 0
    for start, end in intervals:
        total += end - start

    print(int(total))