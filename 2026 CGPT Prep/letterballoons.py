p, t = list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_allow = set(alpha[:p])

teams = []
for _ in range(t):
    team = input()

    if len(team) != len(set(team)):
        continue
    works = True
    for char in team:
        if char not in alpha_allow:
            works = False

    if works:
        teams.append(team)

teams_bits = []
for team in teams:
    mask = 0
    for char in team:
        val = ord(char) - ord('A')
        mask |= (1 << val)
    teams_bits.append(mask)

best = 0
for subset in range(1 << len(teams_bits)):
    works = True
    mask = 0
    count = 0
    for bit in teams_bits:
        if subset & 1:
            count += 1
            if mask & bit:
                works = False
            mask |= bit
        subset >>= 1

    if works:
        best = max(best, count)

print(best)