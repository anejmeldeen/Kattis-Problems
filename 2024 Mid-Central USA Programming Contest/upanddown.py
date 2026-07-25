from bisect import bisect_left

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    longest_ending = {}
    stack = []
    for i, num in enumerate(arr):
        num = arr[i]
        if not stack or stack[-1] < num:
            stack.append(num)
        else:
            idx = bisect_left(stack, num)
            stack[idx] = num
        if stack[-1] == num and len(stack) > 1:
            longest_ending[i] = len(stack)

    longest_ending_rev = {}
    stack = []
    for i in range(n - 1, -1, -1):
        num = arr[i]
        if not stack or stack[-1] < num:
            stack.append(num)
        else:
            idx = bisect_left(stack, num)
            stack[idx] = num
        if stack[-1] == num and len(stack) > 1:
            longest_ending_rev[i] = len(stack)

    best = 0
    for key in longest_ending:
        if key in longest_ending_rev:
            best = max(best, longest_ending[key] + longest_ending_rev[key] - 1)

    print(best)