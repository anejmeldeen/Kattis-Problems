from functools import cache

n, m = list(map(int, input().split()))

pipes = []
for _ in range(m):
    pipes.append(int(input()))

@cache
def recurse(index, location):
    for i in range(location, m):
        pipe = pipes[i]
        if pipe == index:
            return recurse(index + 1, i + 1)
        elif pipe + 1 == index:
            return recurse(index - 1, i + 1)
    return index

res = [0] * n
for num in range(1, n + 1):
    location = recurse(num, 0)
    res[location - 1] = num

for num in res:
    print(num)