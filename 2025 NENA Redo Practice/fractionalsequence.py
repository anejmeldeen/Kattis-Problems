import math
from fractions import Fraction

n = int(input())
a = 1
b = -1
c = - 2 * n

inty = math.ceil((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) - 1

actual = inty * (inty - 1) // 2 + 1

num = n - actual

if num == 0:
    print(inty)
else:
    frac = Fraction(num, inty)
    print(f"{inty} {frac.numerator}/{frac.denominator}")