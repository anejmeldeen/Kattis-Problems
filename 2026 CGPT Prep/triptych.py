from functools import cache
import math

w, d = list(map(int, input().split()))

@cache
def recurse_half(week, a_count, b_count, prev, b_prev_count):
    c_count = week - a_count - b_count

    if week == math.ceil(w / 2):
        if b_prev_count == 2:
            return 0
        if w % 2 == 0:
            if prev in "AC":
                return 0

        a_count *= 2
        b_count *= 2
        c_count *= 2
        if w % 2 == 1:
            if prev == "A":
                a_count -= 1
            elif prev == "B":
                b_count -= 1
            else:
                c_count -= 1
        maxi = max(a_count, b_count, c_count)
        mini = min(a_count, b_count, c_count)
        if maxi - mini <= d:
            return 1
        return 0

    total = 0

    if prev != "A":
        total += recurse_half(week + 1, a_count + 1, b_count, "A", 0)

    if b_prev_count != 2:
        total += recurse_half(week + 1, a_count, b_count + 1, "B", b_prev_count + 1)

    if prev != "C":
        total += recurse_half(week + 1, a_count, b_count, "C", 0)

    return total

@cache
def recurse(week, a_count, b_count, prev, b_prev_count):
    c_count = week - a_count - b_count

    if week == w:
        maxi = max(a_count, b_count, c_count)
        mini = min(a_count, b_count, c_count)
        if maxi - mini <= d:
            return 1
        return 0

    total = 0

    if prev != "A":
        total += recurse(week + 1, a_count + 1, b_count, "A", 0)

    if b_prev_count != 2:
        total += recurse(week + 1, a_count, b_count + 1, "B", b_prev_count + 1)

    if prev != "C":
        total += recurse(week + 1, a_count, b_count, "C", 0)

    return total

print(recurse(0, 0, 0, -1, 0) - recurse_half(0, 0, 0, -1, 0))