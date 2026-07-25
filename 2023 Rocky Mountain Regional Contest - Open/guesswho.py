n, m, q = list(map(int, input().split()))
chars = set()
for idx in range(n):
    chars.add((input(), idx + 1))

for _ in range(q):
    query = input().split()
    idx = int(query[0]) - 1

    rem = set()
    for char in chars:
        if char[0][idx] != query[1]:
            rem.add(char)

    for r in rem:
        chars.remove(r)

if len(chars) == 1:
    print("unique")
    print(chars.pop()[1])
else:
    print("ambiguous")
    print(len(chars))