n, m = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(m + 1)]

for tomes in range(1, m + 1):
    for drops in range(1, n + 1):
        dp[tomes][drops] = 1 + dp[tomes][drops - 1] + dp[tomes - 1][drops - 1]

idx = 0
while True:
    idx += 1
    if dp[m][idx] >= n:
        break

works = []
for pos in range(1, n + 1):
    if dp[m - 1][idx - 1] >= pos - 1 and dp[m][idx - 1] >= n - pos:
        works.append(pos)

add = str(works[0]) if len(works) == 1 else f"{works[0]}-{works[-1]}"
print(idx, add)