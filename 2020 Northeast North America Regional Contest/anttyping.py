from itertools import permutations

number = input()
lenny = len(number)
perms = permutations([x for x in range(1, 10)])

matrix = [[0] * 9 for _ in range(9)]
for i in range(len(number) - 1):
    first, second = int(number[i]), int(number[i + 1])
    matrix[first - 1][second - 1] += 1

best = float('inf')
for perm in perms:
    locations = {e: i for i, e in enumerate(perm)}
    total = lenny + locations[int(number[0])]
    for i in range(9):
        for j in range(9):
            total += matrix[i][j] * abs(locations[i + 1] - locations[j + 1])
    best = min(best, total)

print(best)