from itertools import permutations

n = int(input())
order = [0, 1, 2]

arr = []
for _ in range(n):
    arr.append(int(input()))

best = -1
for tools in permutations(order):
    dp = [[0] * 3 for _ in range(n)]
    curr_tool = 0

    for i in range(n):
        for tool in tools:
            dp[i][tool] = dp[max(0, i - 1)][tool] + (tool == arr[i])
        if arr[i] == tools[1]:
            dp[i][arr[i]] = max(dp[i][arr[i]], dp[max(0, i - 1)][tools[0]] + 1)
        if arr[i] == tools[2]:
            dp[i][arr[i]] = max(dp[i][arr[i]], dp[max(0, i - 1)][tools[0]] + 1, dp[max(0, i - 1)][tools[1]] + 1)

    best = max(best, max(dp[-1]))

print(best)