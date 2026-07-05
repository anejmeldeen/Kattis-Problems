import math
from functools import cache

w, d = list(map(int, input().split()))

@cache
def recurse(week, a_count, b_count, last, streak):
    if week == w:
        c_count = w - a_count - b_count
        if max(a_count, b_count, c_count) - min(a_count, b_count, c_count) > d:
            return 0
        return 1

    ways = 0

    if last != "A":
        ways += recurse(week + 1, a_count + 1, b_count, "A", 0)
    
    if streak <= 1:
        ways += recurse(week + 1, a_count, b_count + 1, "B", streak + 1)
    
    if last != "C":
        ways += recurse(week + 1, a_count, b_count, "C", 0)

    return ways

@cache
def recurse_half(week, a_count, b_count, last, streak):
    if week == w:
        c_count = week - a_count - b_count
        if og_w % 2 == 0:
            full_a = a_count * 2
            full_b = b_count * 2
            full_c = c_count * 2
            
            if last == "A" or last == "C":
                return 0
            if last == "B" and streak == 2:
                return 0
        else:
            full_a = a_count * 2 - (1 if last == "A" else 0)
            full_b = b_count * 2 - (1 if last == "B" else 0)
            full_c = c_count * 2 - (1 if last == "C" else 0)
            
            if last == "B" and streak == 2:
                return 0

        if max(full_a, full_b, full_c) - min(full_a, full_b, full_c) > d:
            return 0
        return 1

    ways = 0

    if last != "A":
        ways += recurse_half(week + 1, a_count + 1, b_count, "A", 0)
    
    if streak <= 1:
        ways += recurse_half(week + 1, a_count, b_count + 1, "B", streak + 1)
    
    if last != "C":
        ways += recurse_half(week + 1, a_count, b_count, "C", 0)

    return ways


sol = recurse(0, 0, 0, -1, 0)
og_w = w
w = math.ceil(w / 2)
palin = recurse_half(0, 0, 0, -1, 0)

print(sol - palin)