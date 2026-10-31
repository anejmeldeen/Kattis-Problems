n = int(input())
arr = list(map(int, input().split()))

killed = set()

curr = 0
for i in range(n - 1):
    size = n - i
    dist = (arr[curr] - 1) % size
    while dist > 0:
        dist -= 1
        curr += 1
        curr %= n
        while curr in killed:
            curr += 1
            curr %= n
    killed.add(curr)
    while curr in killed:
        curr += 1
        curr %= n

print(curr + 1)