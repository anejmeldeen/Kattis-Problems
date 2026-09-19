import math

n, k, p = list(map(int, input().split()))
sol = []

for amt_per_pill in range(1, int(math.sqrt(n) + 1)):
    if n % amt_per_pill != 0:
        continue
    pills = n // amt_per_pill
    if amt_per_pill <= k and pills <= p:
        sol.append(amt_per_pill)
    if pills <= k and amt_per_pill <= p and amt_per_pill != pills:
        sol.append(pills)

sol.sort()
print(len(sol))
for x in sol:
    print(x)