t = int(input())
for _ in range(t):
    n = int(input())
    dists = list(map(int, input().split()))
    dp = [None for _ in range(1001)]
    dp[0] = ([], 0)

    for dist in dists:
        new_dp = [None] * 1001
        for i in range(1001):
            if dp[i] is not None:
                if i - dist >= 0 and (new_dp[i - dist] is None or new_dp[i - dist][1] > dp[i][1]):
                    new_dp[i - dist] = (dp[i][0].copy(), dp[i][1])
                    new_dp[i - dist][0].append("D")
                if i + dist < 1001 and (new_dp[i + dist] is None or new_dp[i + dist][1] > max(dp[i][1], i + dist)):
                    new_dp[i + dist] = (dp[i][0].copy(), max(dp[i][1], i + dist))
                    new_dp[i + dist][0].append("U")
        dp = new_dp
    if dp[0]:
        print(''.join(dp[0][0]))
    else:
        print("IMPOSSIBLE")