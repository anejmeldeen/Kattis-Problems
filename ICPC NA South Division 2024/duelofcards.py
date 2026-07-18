n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
setty = set(cards)

mini = 0
maxi = 0
bob = 0
alice = 0
for card in range(1, 2 * n + 1):
    if card not in setty:
        bob += 1
        if alice > 0:
            mini += 1
            alice -= 1
    else:
        alice += 1
        if bob > 0:
            maxi += 1
            bob -= 1

print(n - mini, maxi)