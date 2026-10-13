n = int(input())
nums = list(map(int, input().split()))
nums.sort()

total = sum(nums)

enemy = nums[-1]
me = nums[-2]
for i in range(n - 2):
    me += nums[i]
    if me > total / 2:
        print(i + 1)
        exit()

print("IMPOSSIBLE TO WIN")