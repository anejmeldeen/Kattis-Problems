n = int(input())

excluded = 0
for _ in range(n):
    num = int(input())
    if num % 2 == 1:
        excluded += 1

print(excluded)