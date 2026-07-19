n = int(input())

green_sets = []
for _ in range(n):
    r, g = list(map(int, input().split()))
    total = r + g
    setty = set()
    for num in range(r, r + g):
        setty.add(num)
    green_sets.append((total, setty))

count = 1
while True:
    possible = True
    for total, setty in green_sets:
        if count % total not in setty:
            possible = False
            break
    if possible:
        print(count)
        break
    count += 1