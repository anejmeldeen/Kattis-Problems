from bisect import bisect_left

n = int(input())
trains = []

for _ in range(n):
    trains.append(int(input()))

lis = []
lds = []
best = 0
lis_map = [0] * n
lds_map = [0] * n
for i in range(n - 1, -1, -1):
    best_lis = 1
    best_lds = 1
    for j in range(i + 1, n):
        if trains[i] < trains[j]:
            best_lis = max(best_lis, 1 + lis_map[j])
        if trains[i] > trains[j]:
            best_lds = max(best_lds, 1 + lds_map[j])
    lis_map[i] = best_lis
    lds_map[i] = best_lds
    best = max(best, best_lis + best_lds - 1)

print(best)