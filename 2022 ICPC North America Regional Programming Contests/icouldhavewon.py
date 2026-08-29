string = input()
sol = []

for k in range(1, len(string) + 1):
    a_wins = 0
    b_wins = 0
    a_count = 0
    b_count = 0
    for char in string:
        if char == "A":
            a_count += 1
        else:
            b_count += 1

        if a_count == k:
            a_count = 0
            b_count = 0
            a_wins += 1
        elif b_count == k:
            a_count = 0
            b_count = 0
            b_wins += 1
    if a_wins > b_wins:
        sol.append(k)
        
print(len(sol))
if sol:
    print(' '.join(list(map(str, sol))))