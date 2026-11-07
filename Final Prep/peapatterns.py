from collections import defaultdict

n, m = input().split()
seen = set([n])

for i in range(100):
    if n == m:
        print(i + 1)
        exit()
    counts = defaultdict(int)
    for char in n:
        counts[char] += 1
    build = []
    for char in "0123456789":
        if counts[char] > 0:
            build.append(str(counts[char]))
            build.append(char)
    n = ''.join(build)

print("Does not appear")