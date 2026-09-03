n = int(input())
maxi = curr = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    curr += b - a
    maxi = max(maxi, curr)
print(maxi)