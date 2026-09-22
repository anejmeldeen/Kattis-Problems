t = int(input())
for _ in range(t):
    target = int(input())
    n = int(input())
    bills = []
    for _ in range(n):
        bills.append(int(input()))

    dp = [float('inf')] * 20001
    dp[0] = 0
    for bill in bills:
        for i in range(20000, -1, -1):
            if dp[i] != float('inf') and i + bill < 20001:
                dp[i + bill] = min(dp[i + bill], dp[i] + 1)

    price = -1
    bills_used = -1
    for i in range(target, 20001):
        if dp[i] != float('inf'):
            price = i
            bills_used = dp[i]
            break

    print(price, bills_used)