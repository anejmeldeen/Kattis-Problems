from functools import cache
import math

while (nums := input()) != "0":
    nums = list(map(int, nums.split()))
    n = nums[0]
    nums = nums[1:]
    nums += nums

    @cache
    def recurse(left, right):
        if left > right:
            return 0
        if right - left == 0:
            return math.gcd(nums[left - 1], nums[left + 1])
        
        best = float('inf')
        gcd_cost = math.gcd(nums[left - 1], nums[right + 1])
        for mid in range(left, right + 1):
            left_rec = recurse(left, mid - 1)
            right_rec = recurse(mid + 1, right)
            cost = gcd_cost + left_rec + right_rec
            best = min(best, cost)
        return best

    res = float('inf')
    for rotation in range(n):
        left = rotation + 1
        right = n - 2 + rotation
        res = min(res, recurse(left, right) + math.gcd(nums[left - 1], nums[right + 1]))

    print(res)