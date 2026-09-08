t = int(input())
for _ in range(t):
    n = int(input())
    counts = {}
    for i in range(n):
        name, count = input().split()
        count = int(count)
        counts[name] = counts.get(name, 0) + count
    sol = []
    for key in counts:
        sol.append((key, counts[key]))
    sol.sort(key=lambda x: (-x[1], x[0]))
    print(len(sol))
    for x in sol:
        print(f"{x[0]} {x[1]}")