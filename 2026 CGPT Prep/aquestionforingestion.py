n, m = list(map(int, input().split()))
food = list(map(int, input().split()))

eat_level = [m]
for _ in range(n - 1):
    eat_level.append(eat_level[-1] * 2 // 3)

dp = [[0] * (n + 1) for _ in range(n + 1)]

for day in range(1, n + 1):
    for m in range(1, n + 1):
        can_eat = min(food[day - 1], eat_level[m - 1])
        dp[m][day] = dp[m][day - 1]
        dp[m][day] = max(dp[m][day], dp[m - 1][day - 1] + can_eat)

        if day >= 2:
            dp[m][day] = max(dp[m][day], dp[m][day - 2] + can_eat)

        if m == 1 and day >= 3:
            for k in range(n + 1):
                dp[m][day] = max(dp[m][day], dp[k][day - 3] + can_eat)

print(max([x[-1] for x in dp]))