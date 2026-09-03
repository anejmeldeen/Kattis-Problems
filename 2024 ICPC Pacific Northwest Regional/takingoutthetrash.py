n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

count = 0
left = 0
right = n - 1
while left < right:
    if arr[left] + arr[right] <= m:
        left += 1
    count += 1
    right -= 1

print(count + (left == right))