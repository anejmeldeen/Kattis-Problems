n, x, y = list(map(int, input().split()))
mult = y / x
for _ in range(n):
    num = int(input())
    print(round(num * mult))