n = int(input())
people = []

for _ in range(n):
    availability = []
    data = list(map(int, input().split()))
    m = data[0]
    idx = 1
    for _ in range(m):
        left = data[idx]
        right = data[idx + 1]
        availability.append((left, right))
        idx += 2
    people.append(availability)

best = 0
best_count = 0
for time in range(0, 86401):
    curr = 0
    for person in people:
        for window in person:
            if window[0] <= time and time <= window[1]:
                curr += 1
                break
    if curr > best:
        best = curr
        best_count = 1
    elif curr == best:
        best_count += 1

print(best)
print(best_count)