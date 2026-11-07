import math

r, s, h = list(map(int, input().split()))

circum = 2 * math.pi * r
days = circum / s / h

fraction = days % 1
print(fraction)

amount = 1 / fraction
print(amount)

fraction = amount % 1
amount = 1 / fraction
print(amount)

fraction = amount % 1
amount = 1 / fraction
print(amount)