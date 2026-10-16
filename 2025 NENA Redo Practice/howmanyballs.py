import math

p, q = list(map(int, input().split()))

for r in range(1, 1000001):
    a = p
    b = 2 * p * r - p - 2 * r * q
    c = p * r ** 2 - p * r

    g = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if g % 1 == 0:
        print(r, int(g))
        exit()

print("impossible")