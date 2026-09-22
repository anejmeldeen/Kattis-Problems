n = int(input())
weights = []

for _ in range(n):
    weights.append(int(input()))

dp = [False] * 2000
dp[0] = True

for w in weights:
    for i in range(1999, -1, -1):
        if dp[i] and i + w < 2000:
            dp[i + w] = True

dist = 0
while True:
    if dp[1000 + dist]:
        print(1000 + dist)
        break
    elif dp[1000 - dist]:
        print(1000 - dist)
        break
    dist += 1