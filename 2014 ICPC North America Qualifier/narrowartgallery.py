while True:
    n, k = list(map(int, input().split()))
    if n == 0 and k == 0:
        break

    gallery = []
    for _ in range(n):
        nums = list(map(int, input().split()))
        gallery.append(nums)

    dp = [[float('-inf')] * (k + 1) for _ in range(3)]
    dp[0][0] = 0
    
    for i in range(n):
        new_dp = [[float('-inf')] * (k + 1) for _ in range(3)]
        for closed in range(k + 1):
            new_dp[0][closed] = max([dp[i][closed] for i in range(3)]) + gallery[i][0] + gallery[i][1]

            if closed != k:
                new_dp[1][closed + 1] = max(dp[0][closed], dp[1][closed]) + gallery[i][0]
                new_dp[2][closed + 1] = max(dp[0][closed], dp[2][closed]) + gallery[i][1]

        dp = new_dp
    
    best = -1
    for state in range(3):
        best = max(best, dp[state][k])

    print(best)