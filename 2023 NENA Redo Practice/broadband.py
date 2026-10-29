n, m, k, s = list(map(int, input().split()))
n += m

locations = list(map(float, input().split()))
locations += list(map(float, input().split()))

locations.sort()

dp = [float('inf')] * (n + 1)
dp[0] = 0

pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + locations[i - 1] ** 2

pref_norm = [0] * (n + 1)
for i in range(1, n + 1):
    pref_norm[i] = pref_norm[i - 1] + locations[i - 1]

for _ in range(k):
    new_dp = [float('inf')] * (n + 1)
    new_dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            average = pref_norm[i] - pref_norm[j]
            average /= (i - j)
            calculation = pref[i] - pref[j]
            calculation += -2 * average * (pref_norm[i] - pref_norm[j])
            calculation += average ** 2 * (i - j)
            new_dp[i] = min(new_dp[i], dp[j] + calculation)

    dp = new_dp

print(dp[-1] + n * (s / 2) ** 2)