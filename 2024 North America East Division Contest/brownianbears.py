from fractions import Fraction

n, x, y, d = list(map(int, input().split()))

dp = [[Fraction(0, 1)] * n for _ in range(n)]
dp[x - 1][y - 1] = Fraction(1, 1)

total = Fraction(0, 1)
for _ in range(d):
    new_dp = [[Fraction(0, 1)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            odd = dp[i][j]
            new_dp[max(0, i - 1)][max(0, j - 1)] += odd / 4
            new_dp[min(n - 1, i + 1)][max(0, j - 1)] += odd / 4
            new_dp[max(0, i - 1)][min(n - 1, j + 1)] += odd / 4
            new_dp[min(n - 1, i + 1)][min(n - 1, j + 1)] += odd / 4

    for x in range(n):
        total += new_dp[x][x]
        new_dp[x][x] = Fraction(0, 1)
    dp = new_dp

print(f"{total.numerator}/{total.denominator}")