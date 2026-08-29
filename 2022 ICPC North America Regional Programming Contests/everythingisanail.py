from itertools import permutations

n = int(input())
moves = []
for _ in range(n):
    moves.append(int(input()))

best = 0
for perm in permutations([0, 1, 2]):
    dp = [[0] * n for _ in range(3)]
    for i, move in enumerate(moves):
        dp[0][i] = dp[0][i - 1] if i > 0 else 0
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 1]) if i > 0 else 0
        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1]) if i > 0 else 0

        if perm[0] == move:
            dp[0][i] += 1
        elif perm[1] == move:
            dp[1][i] += 1
        else:
            dp[2][i] += 1

    best = max(best, dp[0][-1], dp[1][-1], dp[2][-1])

print(best)