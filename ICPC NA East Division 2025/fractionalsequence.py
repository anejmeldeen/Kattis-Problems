import math

n = int(input())

a = 1
b = -1
c = (n - 1) * -2

sol = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
inty = int(sol)

actual_n = (inty ** 2 - inty) // 2 + 1
diff = n - actual_n

num = diff
denom = inty
g = math.gcd(num, denom)
num //= g
denom //= g

if diff == 0:
    print(inty)
else:
    print(f"{inty} {num}/{denom}")