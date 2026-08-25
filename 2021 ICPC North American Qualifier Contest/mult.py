n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

sol = []
first = -1
for i in range(n):
    if first == -1:
        first = nums[i]
        continue
    if nums[i] % first == 0 and nums[i] >= first:
        sol.append(nums[i])
        first = -1

for x in sol:
    print(x)