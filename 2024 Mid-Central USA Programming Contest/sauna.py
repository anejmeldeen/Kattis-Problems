n = int(input())
mini = float('-inf')
maxi = float('inf')
for _ in range(n):
    a, b = list(map(int, input().split()))
    maxi = min(maxi, b)
    mini = max(mini, a)

if mini <= maxi:
    print(maxi - mini + 1, end=" ")
    print(mini)
else:
    print("bad news")