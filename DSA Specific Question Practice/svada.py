t = int(input())

n = int(input())
first_monk = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    first_monk.append((a, b))

m = int(input())
second_monk = []

for _ in range(m):
    a, b = list(map(int, input().split()))
    second_monk.append((a, b))

left = 1
right = t - 1

while left <= right:
    mid = (left + right) // 2

    possible = True
    first_time = mid
    second_time = t - mid

    produced = 0
    opened = 0

    for i in range(n):
        a, b = first_monk[i]
        if first_time >= a:
            produced += 1
        if first_time - a >= b:
            produced += (first_time - a) // b
    for i in range(m):
        a, b = second_monk[i]
        if second_time >= a:
            opened += 1
        if second_time - a >= b:
            opened += (second_time - a) // b

    if opened >= produced:
        left = mid + 1
    else:
        right = mid - 1

print(right)