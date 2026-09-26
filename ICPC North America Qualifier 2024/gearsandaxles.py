import math

n = int(input())

gears = []
for _ in range(n):
    s, c = list(map(int, input().split()))
    gears.append((s, c))

size_to_teeth = {}
for s, c in gears:
    if s not in size_to_teeth:
        size_to_teeth[s] = []
    size_to_teeth[s].append(c)

total = 0
for size in size_to_teeth:
    arr = size_to_teeth[size]
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        total += math.log(arr[right] / arr[left])
        left += 1
        right -= 1

print(total)