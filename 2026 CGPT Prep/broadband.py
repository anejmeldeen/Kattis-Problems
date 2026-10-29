m, n, k, s = list(map(int, input().split()))

first = list(map(float, input().split()))
second = list(map(float, input().split()))
points = first + second

points.sort()

prefix_sum = [0] * (len(points) + 1)
prefix_sum_squared = [0] * (len(points) + 1)

for i in range(1, len(points) + 1):
    prefix_sum[i] = prefix_sum[i - 1] + points[i - 1]
    prefix_sum_squared[i] = prefix_sum_squared[i - 1] + points[i - 1] ** 2

dp = [[float('inf')] * (k + 1) for _ in range(len(points) + 1)]
dp[0][0] = 0

for i in range(1, len(points) + 1):
    for p in range(i):
        num_points = i - p
        add_cost = (prefix_sum_squared[i] - prefix_sum_squared[p]) - (prefix_sum[i] - prefix_sum[p]) ** 2 / num_points
        for j in range(1, k + 1):
            prev = dp[p][j - 1]
            dp[i][j] = min(dp[i][j], prev + add_cost)

print(dp[-1][-1] + (s / 2) ** 2 * len(points))