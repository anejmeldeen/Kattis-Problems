t, s = list(map(int, input().split()))

t_dots = (t + 1) ** 2 + (t ** 2)
s_dots = (s + 1) ** 2 + (s ** 2)

add = 0
curr_add = 1
curr_row = 1
for new_s in range(3, s + 1):
    add += curr_add
    curr_row += 1

    if curr_row == 4:
        curr_row == 1
        curr_add += 1

s_dots += add * 4

import math
g = math.gcd(t_dots, s_dots)
t_dots //= g
s_dots //= g

if t_dots >= s_dots:
    print(1)
else:
    print(f"{t_dots}/{s_dots}")