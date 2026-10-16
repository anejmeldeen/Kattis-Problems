from functools import cache
import math

w, d = list(map(int, input().split()))

@cache
def num_ways_half(week, a_count, b_count, prev, b_prev_count):
    c_count = week - a_count - b_count

    if week == math.ceil(w / 2):
        if w % 2 == 0:
            if prev == "A" or prev == "C":
                return 0
        if b_prev_count == 2:
            return 0

        a_count *= 2
        b_count *= 2
        c_count *= 2
        if w % 2 == 1:
            if prev == "A":
                a_count -= 1
            if prev == "B":
                b_count -= 1
            if prev == "C":
                c_count -= 1
        if abs(a_count - b_count) > d or abs(b_count - c_count) > d or abs(c_count - a_count) > d:
            return 0

        return 1

    total = 0

    if prev != "A":
        total += num_ways_half(week + 1, a_count + 1, b_count, "A", 1 if prev == "B" else 0)

    if b_prev_count < 2:
        total += num_ways_half(week + 1, a_count, b_count + 1, "B", 2 if prev == "B" else 1)

    if prev != "C":
        total += num_ways_half(week + 1, a_count, b_count, "C", 1 if prev == "B" else 0)

    return total

@cache
def num_ways(week, a_count, b_count, prev, b_prev_count):
    c_count = week - a_count - b_count

    if week == w:
        if abs(a_count - b_count) > d or abs(b_count - c_count) > d or abs(c_count - a_count) > d:
            return 0
        return 1

    total = 0

    if prev != "A":
        total += num_ways(week + 1, a_count + 1, b_count, "A", 1 if prev == "B" else 0)

    if b_prev_count < 2:
        total += num_ways(week + 1, a_count, b_count + 1, "B", 2 if prev == "B" else 1)

    if prev != "C":
        total += num_ways(week + 1, a_count, b_count, "C", 1 if prev == "B" else 0)

    return total

print(num_ways(0, 0, 0, 0, 0) - num_ways_half(0, 0, 0, 0, 0))