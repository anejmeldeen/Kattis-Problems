n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

get_cals = [m]
for _ in range(n - 1):
    val = get_cals[-1] * 2 // 3
    get_cals.append(val)

for day in range(1, n + 1):
    for m_val in range(1, n + 1):
        calories = min(get_cals[m_val - 1], arr[day - 1])
        dp[m_val][day] = max(dp[m_val][day - 1], dp[m_val - 1][day - 1] + calories)
        dp[m_val][day] = max(dp[m_val][day], dp[m_val][day - 2] + calories) # account for skipping one day

        # account for skipping 2 days
        if m_val == 1:
            for other_m_val in range(1, n + 1):
                dp[1][day] = max(dp[1][day], dp[other_m_val][day - 3] + calories)

print(max([row[-1] for row in dp]))