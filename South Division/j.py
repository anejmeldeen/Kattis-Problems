import math

u = int(input())

prime_factors = []
for i in range(2, int(math.sqrt(u)) + 1):
    while u % i == 0:
        prime_factors.append(i)
        u //= i
if u != 1:
    prime_factors.append(u)

summ = 1
product = 1
prime_factors.sort(reverse=True)
prime_factors.pop()

for x in prime_factors:
    product *= x
    summ += product

print(summ)