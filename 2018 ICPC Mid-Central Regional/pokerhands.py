cards = input().split()
counts = {}

most = 0
for card in cards:
    counts[card[0]] = counts.get(card[0], 0) + 1
    most = max(most, counts[card[0]])

print(most)