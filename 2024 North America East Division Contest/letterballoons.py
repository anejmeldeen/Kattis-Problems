p, t = list(map(int, input().split()))
letter_set = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter_to_pos = {e: i for i, e in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
letter_set = set(letter_set[:p])

teams = []
for _ in range(t):
    team = input()
    possible = True
    
    if len(set(team)) != len(team):
        possible = False
    for char in team:
        if char not in letter_set:
            possible = False

    if possible:
        teams.append(team)

t = len(teams)
teams = [set(x) for x in teams]
new_teams = []
for team in teams:
    num = 0
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char in team:
            num |= (1 << letter_to_pos[char])
    new_teams.append(num)
teams = new_teams

best = 0
for subset in range(1 << t):
    possible = True
    letters = set()
    count = 0
    taken = 0
    for i in range(t):
        if subset & 1:
            if taken & teams[i]:
                possible = False
            taken = teams[i] | taken
            count += 1
        subset >>= 1
    if possible:
        best = max(best, count)

print(best)