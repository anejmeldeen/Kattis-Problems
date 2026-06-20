n = int(input())
intervals = []
for _ in range(n):
    intervals.append(tuple(map(int, input().split())))

intervals.sort()

total = 0

prev_start = -1
prev_end = -1
for start, end in intervals:
    if (prev_start <= start and start <= prev_end) or (start <= prev_start and prev_start <= end):
        prev_start = max(start, prev_start)
        prev_end = min(end, prev_end)
    else:
        prev_start = start
        prev_end = end
        total += 1

print(total)