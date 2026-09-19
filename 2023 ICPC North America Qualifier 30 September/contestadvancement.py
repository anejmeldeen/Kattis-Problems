n, k, c = list(map(int, input().split()))

counts = {}
sol = []
others = []
for r in range(n):
    t, s = list(map(int, input().split()))
    if s not in counts or counts[s] < c:
        if len(sol) < k:
            counts[s] = counts.get(s, 0) + 1
            sol.append((t, r))
    else:
        others.append((t, r))

for i in range(k - len(sol)):
    sol.append(others[i])

sol.sort(key=lambda x: x[1])

for x in sol:
    print(x[0])