from fractions import Fraction

n, x, y, d = list(map(int, input().split()))

total = Fraction(0, 1)
dp = [[Fraction(0)] * n for _ in range(n)]

dp[x - 1][y - 1] = Fraction(1)

for _ in range(d):
    new_dp = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            prob = dp[i][j]
            x1 = max(0, i - 1)
            x2 = min(n - 1, i + 1)
            y1 = max(0, j - 1)
            y2 = min(n - 1, j + 1)
            add = prob / 4
            new_dp[x1][y1] += add * 1
            new_dp[x1][y2] += add * 1
            new_dp[x2][y1] += add * 1
            new_dp[x2][y2] += add * 1

    for i in range(n):
        total += new_dp[i][i]
        new_dp[i][i] = Fraction(0)

    dp = new_dp

print(f"{total.numerator}/{total.denominator}")