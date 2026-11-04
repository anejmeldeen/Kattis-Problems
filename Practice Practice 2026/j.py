import math

n = int(input())

costs = list(map(int, input().split()))
bit_sets = []

def factorize(n):
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        while n % i == 0:
            n //= i
            if i > 53:
                continue
            factors.add(i)
    if n != 1 and n <= 53:
        factors.add(n)
    return factors

add = costs[0]
costs = costs[1:]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
prime_to_idx = {e: i for i, e in enumerate(primes)}

for i in range(2, n + 1):
    prime_factorization = factorize(i)
    mask = 0
    for prime in prime_factorization:
        mask |= (1 << prime_to_idx[prime])
    bit_sets.append(mask)

dp = [[float('-inf')] * (n) for _ in range(2 ** len(primes))]
for i in range(n):
    dp[0][i] = 0

for i in range(2 ** len(primes)):
    for j in range(1, n):
        bits_need = bit_sets[j - 1]
        dp[i][j] = dp[i][j - 1]
        if i & bits_need != bits_need:
            continue
        mask = i & (~bits_need)
        dp[i][j] = max(dp[i][j - 1], dp[mask][j - 1] + costs[j - 1])

best = max([dp[i][-1] for i in range(2 ** (len(primes)))])

print(best + add)