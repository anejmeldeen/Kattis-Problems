n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

word = input()

char_map = {e:i for i, e in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")}
rev_map = {i:e for i, e in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")}
res = []

for char in word:
    res.append(char_map[char])

while len(res) % n != 0:
    res.append(36)

matrix_prod = []
idx = 0
for idx in range(0, len(res), n):
    for row in matrix:
        count = 0
        for i in range(len(row)):
            count += row[i] * res[i + idx]
            count %= 37
        matrix_prod.append(count)

res = []
for num in matrix_prod:
    res.append(rev_map[num])
print(''.join(res))