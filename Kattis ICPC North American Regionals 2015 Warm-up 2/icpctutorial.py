import math
m, n, t = list(map(int, input().split()))

passed = True

if t == 1:
    prod = 1
    for i in range(1, n + 1):
        prod *= i
        if prod > m:
            passed = False
            break
elif t == 2:
    passed = (2 ** n) <= m
elif t == 3:
    passed = (n ** 4) <= m
elif t == 4:
    passed = (n ** 3) <= m
elif t == 5:
    passed = (n ** 2) <= m
elif t == 6:
    passed = (n * math.log2(n)) <= m
else:
    passed = n <= m

print("AC" if passed else "TLE")