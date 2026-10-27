from collections import defaultdict
from itertools import permutations

board = list(input())
arr = list(map(int, input().split()))

deletions = list(map(int, input().split()))
for delete in deletions[1:]:
    board[delete - 1] = "X"
    arr[delete - 1] = 0

add = list(input())
if add[0] == "X":
    add = []

char_to_num = {e: i for i, e in enumerate("AEIOU")}
num_to_char = {i: e for i, e in enumerate("AEIOU")}

need_size = defaultdict(int)
for char in board:
    if char != "X":
        need_size[char_to_num[char]] += 1
for char in add:
    need_size[char_to_num[char]] += 1

total_cost = sum(arr)
n = len(board)
prefixes = [[0] * (n + 1) for _ in range(5)]
for i in range(5):
    for j in range(1, n + 1):
        add = 0
        if board[j - 1] == num_to_char[i]:
            add = arr[j - 1]
        prefixes[i][j] = prefixes[i][j - 1] + add

best = 0

for perm in permutations([0, 1, 2, 3, 4]):
    dp = [[float('-inf')] * (n + 1) for _ in range(6)]
    for i in range(n + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for c in range(1, 6):
            letter = perm[c - 1]
            dp[c][i] = dp[c][i - 1]

            length = need_size[letter]
            if i - length >= 0:
                dp[c][i] = max(dp[c][i], dp[c - 1][i - length] + prefixes[letter][i] - prefixes[letter][i - length])

    best = max(best, dp[-1][-1])

print(total_cost - best)