arr = list(map(int, input().split()))
n = arr[0]
nums = arr[1:]

maxes = [float('-inf')] * (n + 1)
minis = [float('inf')] * (n + 1)

for i in range(1, n + 1):
    maxes[i] = max(maxes[i - 1], nums[i - 1])
for i in range(n - 1, -1, -1):
    minis[i] = min(minis[i + 1], nums[i])

sol = []
for i, num in enumerate(nums):
    if num >= maxes[i] and num <= minis[i]:
        sol.append(num)

print(f"{len(sol)} " + ' '.join(list(map(str, sol[:100]))))