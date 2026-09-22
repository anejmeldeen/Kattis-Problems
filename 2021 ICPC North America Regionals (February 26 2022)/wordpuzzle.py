p = input()
og_s = list(input())

MOD = 1000000007

seen = set()
total = 0
for rotate in range(len(og_s)):
    s = og_s[rotate:] + og_s[:rotate]
    if tuple(s) in seen:
        continue
    seen.add(tuple(s))

    dp = [0] * (len(s) + 1)
    dp[0] = 1

    for char in p:
        for i in range(len(s) - 1, -1, -1):
            if s[i] == char:
                dp[i + 1] += dp[i]
                dp[i + 1] %= MOD
    total += dp[-1]
    total %= MOD

print(total)