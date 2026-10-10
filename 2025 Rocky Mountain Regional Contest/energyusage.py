n, m, b = list(map(int, input().split()))

prices = []
for _ in range(n):
    p, r, s = list(map(int, input().split()))
    prices.append((p, r, s))

plan_payment = []
for _ in range(n):
    data = list(map(int, input().split()))
    plan_payment.append(data + [0])

plan_cost = []
for _ in range(n):
    data = list(map(int, input().split()))
    plan_cost.append(data + [0])

dp = [float('inf')] * (b + 1)
dp[0] = 0

for day in range(n):
    p, r, s = prices[day]
    new_dp = [float('inf')] * (b + 1)

    for energy_in in range(b + 1):
        for energy_out in range(b + 1):
            for plan in range(m + 1):
                money_saved = plan_payment[day][plan]
                energy_plan_used = plan_cost[day][plan]

                energy_have = energy_in + s
                energy_need = energy_out + energy_plan_used + r
                old_cost = dp[energy_in]
                new_cost = old_cost - money_saved

                diff = energy_need - energy_have
                if diff > 0:
                    new_cost += diff * p

                new_dp[energy_out] = min(new_dp[energy_out], new_cost)

    dp = new_dp

print(dp[0])