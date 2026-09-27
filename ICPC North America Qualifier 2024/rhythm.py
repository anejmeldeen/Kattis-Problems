n, m = list(map(int, input().split()))
expected = []
actual = []

for _ in range(n):
    expected.append(int(input()))
for _ in range(m):
    actual.append(int(input()))

def get_value(x):
    if x > 102:
        return 0
    elif x > 43:
        return 2
    elif x > 23:
        return 4
    elif x > 15:
        return 6
    else:
        return 7
    

dp = [[0] * (len(actual) + 1) for _ in range(len(expected) + 1)]
for i in range(1, len(expected) + 1):
    for j in range(1, len(actual) + 1):
        skip_expected = dp[i - 1][j]
        skip_actual = dp[i][j - 1]
        take = dp[i - 1][j - 1] + get_value(abs(expected[i - 1] - actual[j - 1]))
        dp[i][j] = max(skip_actual, skip_expected, take)

print(dp[-1][-1])