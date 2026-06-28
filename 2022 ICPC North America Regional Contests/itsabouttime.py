import math

r, s, h = list(map(int, input().split()))
circum = 2 * math.pi * r
hours_to_rotate = circum / s
days_in_year = hours_to_rotate / h

d = math.floor(days_in_year + 0.5)
extra_time = abs(d - days_in_year)

b_n1 = -1
b_n2 = -1
b_n3 = -1
small_diff = float('inf')
for n1 in range(2, 1001):
    for n2 in range(n1 + n1, 1001, n1):
        for n3 in range(n2 + n2, 1001, n2):
            diff = abs((1 / n1) - (1 / n2) + (1 / n3) - extra_time)
            if diff < small_diff:
                small_diff = diff
                b_n1 = n1
                b_n2 = n2
                b_n3 = n3

print(b_n1, b_n2, b_n3)