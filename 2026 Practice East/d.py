import math

t = int(input())
for _ in range(t):
    r, p, q, l, u = list(map(int, input().split()))

    a = p
    b = 2 * p * r - p - 2 * r * q
    c = p * r ** 2 - p * r

    b = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(b)