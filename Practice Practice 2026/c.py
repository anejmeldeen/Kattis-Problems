n, s, b0, m = list(map(int, input().split()))

outcomes = input()

strategies = []
for _ in range(s):
    data = input().split()
    arr = []
    for i in range(0, 2 * n, 2):
        arr.append((data[i], int(data[i + 1])))
    strategies.append(arr)

best_outcome = -float('inf')
best_strat = -1
for j, strat in enumerate(strategies):
    money = b0
    for i, day in enumerate(strat):
        guess, wager = day
        actual = outcomes[i]
        if money - wager >= m:
            if actual == guess:
                money += wager
            else:
                money -= wager
    if money > best_outcome:
        best_outcome = money
        best_strat = j

print(best_strat + 1, best_outcome)