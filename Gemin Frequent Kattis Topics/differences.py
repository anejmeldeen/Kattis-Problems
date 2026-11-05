a1, m = list(map(int, input().split()))

seen = set()
sequence = set()
sequence.add(a1)
seen.add(a1)

d = 1
iterations = 1
curr = a1
while curr != m and m not in seen:
    iterations += 1
    while d in seen:
        d += 1

    curr = curr + d
    seen.add(curr)
    for item in sequence:
        seen.add(curr - item)
    sequence.add(curr)

print(iterations)