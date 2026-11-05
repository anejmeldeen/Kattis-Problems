n = int(input())

res = []
seen = set()
for i in range(n):
    items = input().split()[1:]
    for item in items:
        if item not in seen:
            seen.add(item)
            res.append(item)
            break

print(' '.join(res))