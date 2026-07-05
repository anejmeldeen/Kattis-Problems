import math

p, q = list(map(int, input().split()))

found = False
for r in range(1, int(1e6) + 1):
    a = p
    b = 2*p*r - p - 2*r*q
    c = p*(r ** 2) - r*p

    root = (-b + math.sqrt(b ** 2 - 4*a*c)) / (2*a)
    if root % 1 == 0:
        print(r, int(root))
        found = True
        break

if not found:
    print("impossible")