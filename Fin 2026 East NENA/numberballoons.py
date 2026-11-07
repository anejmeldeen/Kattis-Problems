p, t = list(map(int, input().split()))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = alphabet[:p]
char_to_num = {e: i for i, e in enumerate(alphabet)}

teams = []
for _ in range(t):
    team = input()
    if len(team) != len(set(team)):
        continue
    get_out = False
    for char in team:
        if char not in alphabet:
            get_out = True
    if get_out:
        continue

    mask = 0
    for char in team:
        num = char_to_num[char]
        mask |= (1 << num)

    teams.append(mask)

t = len(teams)

best = 0
for subset in range(1 << t):
    curr = 0
    use = []
    idx = 0
    while subset > 0:
        if subset & 1:
            use.append(teams[idx])
            curr += 1
        idx += 1
        subset >>= 1

    works = True
    mask = 0
    for team in use:
        if mask & team:
            works = False
        mask |= team

    if works:
        best = max(best, curr)

print(best)