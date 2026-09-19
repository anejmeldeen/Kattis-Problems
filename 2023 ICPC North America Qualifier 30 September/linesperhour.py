n, speed = list(map(int, input().split()))
nums = []
for _ in range(n):
    nums.append(int(input()))

speed *= 5
nums.sort()
count = 0
summ = 0
for i in range(n):
    if summ + nums[i] <= speed:
        summ += nums[i]
        count += 1

print(count)