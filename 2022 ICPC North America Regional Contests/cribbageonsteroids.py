import math

n = int(input())
arr = []

while len(arr) < n:
    arr += input().split()

arr = arr[:n]

key_dict = {e: i for i, e in enumerate("A23456789TJQK")}
num_dict = {i: e for i, e in enumerate("A23456789TJQK")}
value_dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10}
arr.sort(key=lambda x: key_dict[x])

counts = {}
for card in arr:
    counts[card] = counts.get(card, 0) + 1

ans = 0

# count pairs
for key in counts:
    ans += counts[key] * (counts[key] - 1)

# count runs
curr_run_count = 0
run_len = 0
prev = -1
for num in range(13):
    card = num_dict[num]
    cont = False

    if card not in counts:
        cont = True
    else:
        if run_len == 0:
            run_len = 1
            curr_run_count = counts[card]
        else:
            if num_dict[key_dict[prev] + 1] == card:
                run_len += 1
                curr_run_count *= counts[card]
            else:
                cont = True

    if cont:
        if run_len >= 3:
            ans += curr_run_count * run_len
        curr_run_count = 0
        run_len = 0
    prev = card

if run_len >= 3:
    ans += curr_run_count * run_len

# count 15 counts
dp = [[0] * (16) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for c in range(15, -1, -1):
        card_val = value_dict[arr[i - 1]]
        if c - card_val >= 0:
            dp[i][c] += dp[i - 1][c - card_val]
        dp[i][c] += dp[i - 1][c]

ans += dp[n][15] * 2

print(ans)