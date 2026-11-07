from collections import defaultdict

n = int(input())

hand = []
while len(hand) < n:
    hand += input().split()

evaluate = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 10, "K": 10, "Q": 10}
order = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "K": 13, "Q": 12}
hand.sort(key=lambda x: order[x])

pairs = 0
counts = defaultdict(int)
for card in hand:
    counts[card] += 1
for key in counts:
    pairs += counts[key] * (counts[key] - 1) // 2
pairs *= 2

dp = [0] * 16
dp[0] = 1
for card in hand:
    num = evaluate[card]
    for j in range(15, -1, -1):
        if j + num <= 15:
            dp[j + num] += dp[j]

fifteens = dp[15] * 2

runs = 0
prev = -100
mult = 1
curr_mult = 1
length = 0
hand.append(100000)
for card in hand:
    num = order[card] if card in order else 100000
    if num == prev:
        curr_mult += 1
    elif num == prev + 1:
        mult *= curr_mult
        curr_mult = 1
        length += 1
    else:
        if length >= 3:
            runs += length * mult * curr_mult
        length = 1
        mult = 1
        curr_mult = 1

    prev = num

print(pairs + fifteens + runs)