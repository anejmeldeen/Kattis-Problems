n, k = list(map(int, input().split()))
setty = set()

for _ in range(n):
    setty.add(int(input()))

print(min(len(setty), k))