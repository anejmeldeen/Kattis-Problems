from collections import deque

m, s = list(map(int, input().split()))

starting = tuple(map(int, input().split()))
ending = tuple(map(int, input().split()))

intervals = []
for _ in range(s):
    intervals.append(list(map(int, input().split())))


queue = deque([(starting, 0)])
seen = set([starting])
res = -1
while queue:
    orientation, dist = queue.popleft()
    if orientation == ending:
        res = dist
        break
    seen.add(orientation)

    mini = float('inf')
    for a, b in intervals:
        b = (a + b) % m
        b -= 1
        new_orientation = list(orientation)
        last = new_orientation[b]
        while b != a:
            prev = (b - 1) % m
            new_orientation[b] = new_orientation[prev]
            b = prev
        new_orientation[a] = last
        if tuple(new_orientation) not in seen:
            queue.append((tuple(new_orientation), dist + 1))
            seen.add(tuple(new_orientation))

print(res)