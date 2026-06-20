n, k = list(map(int, input().split()))
subs = []
for _ in range(n):
    subs.append(input())

best_lowest = 0
for i in range(1 << k):
    lowest = k
    for sub in subs:
        this_one = 0
        for j in range(k):
            dig = 1 & (i >> (k - j - 1))
            if (dig and sub[j] == "T") or (not dig and sub[j] == "F"):
                this_one += 1
        lowest = min(lowest, this_one)

    best_lowest = max(best_lowest, lowest)

print(best_lowest)