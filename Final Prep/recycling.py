n = int(input())
nums = []

while len(nums) < n:
    nums += list(map(int, input().split()))

nums.append(float('-inf'))

stack = [(float('-inf'), -1)]
best = -1
left_ans = right_ans = -1
for right, num in enumerate(nums):
    while stack and stack[-1][0] > num:
        prev_num, idx = stack.pop()
        dist = right - stack[-1][1] - 1
        total = (dist) * prev_num
        if total > best:
            best = total
            left_ans = stack[-1][1] + 1
            right_ans = right - 1
        elif total == best:
            if (stack[-1][1] + 1 < left_ans):
                left_ans = stack[-1][1] + 1
                right_ans = right - 1
    stack.append((num, right))

print(left_ans + 1, right_ans + 1, best)