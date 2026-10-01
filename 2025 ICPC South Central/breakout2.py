n, x, c = list(map(int, input().split()))
count = 0

for _ in range(c):
    num = int(input())
    if num < x:
        count += 1

print(min(count, c - count))