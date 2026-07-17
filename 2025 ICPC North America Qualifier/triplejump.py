n = int(input())
arr = list(map(int, input().split()))

lowest = arr[0] // 3
highest = arr[-1] // 3
medium = arr[1] - lowest * 2

print(lowest, medium, highest)