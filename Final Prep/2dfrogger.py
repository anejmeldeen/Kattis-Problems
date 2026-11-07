from fractions import Fraction
from functools import cache

m, n, p = list(map(int, input().split()))

@cache
def recurse(a, b, k):
    c = n - a - b
    d = (m - 2 * n) - (k - 2 * a - b)

    total_squares = 2 * c + b + d

    if b > n or a > n or b < 0 or a < 0 or d < 0:
        return 0

    if k == p:
        if a + b == n:
            return 1
        return 0

    ways = Fraction(0)
    if a + b != n:
        ways += Fraction(b, total_squares) * recurse(a + 1, b - 1, k + 1)
        ways += Fraction(d, total_squares) * recurse(a, b, k + 1)
    ways += Fraction(2 * c, total_squares) * recurse(a, b + 1, k + 1)

    return ways

frac = recurse(0, 0, 0)
print(f"{frac.numerator}/{frac.denominator}")