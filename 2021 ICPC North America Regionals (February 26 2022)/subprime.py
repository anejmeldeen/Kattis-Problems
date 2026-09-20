import math

MAXI = int(5 * 1e6)
sieve = [True] * MAXI
sieve[1] = False

for i in range(2, int(math.sqrt(MAXI)) + 1):
    for j in range(i * i, MAXI, i):
        sieve[j] = False

l, h = list(map(int, input().split()))

primes = []
for i in range(2, MAXI):
    if sieve[i]:
        primes.append(i)
    if len(primes) >= h:
        break

p = input()
count = 0
primes = primes[l - 1:h]
for pr in primes:
    if p in str(pr):
        count += 1

print(count)