n = int(input())
additional = list(map(int, input().split()))
solves = list(map(int, input().split()))

best = 0
solves.sort(reverse=True)

total = 0
for i in range(n):
    total += solves[i]
    best = max(best, (total + additional[i]) / (i + 1))

print(best)