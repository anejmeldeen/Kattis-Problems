n, m = list(map(int, input().split()))
coins = set(map(int, input().split()))
MAX = int(10 ** 5)

queries = []
for _ in range(m):
    query = input().split()
    if query[0] == "X":
        coins.remove(int(query[1]))
    queries.append(query)

queries = queries[::-1]
sol = []

dp = [float('inf')] * (MAX + 1)
dp[0] = 0

for coin in coins:
    for i in range(MAX + 1):
        if (i + coin) <= MAX:
            dp[i + coin] = min(dp[i + coin], dp[i] + 1)

for q in queries:
    c, v = q
    v = int(v)

    if c == "Q":
        sol.append(-1 if dp[v] == float('inf') else dp[v])
    else:
        for i in range(MAX + 1):
            if i + v <= MAX:
                dp[i + v] = min(dp[i + v], dp[i] + 1)

sol = sol[::-1]
for x in sol:
    print(x)