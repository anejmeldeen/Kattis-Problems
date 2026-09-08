t = int(input())
for _ in range(t):
    n = int(input())
    curr = 1
    for x in range(1, n + 1):
        curr *= x
        curr %= 10
    print(curr)