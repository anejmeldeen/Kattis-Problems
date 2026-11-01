import math
3
n, l = list(map(int, input().split()))

pieces = []
total = 0
sub_total = 0
for _ in range(n):
    a, q = list(map(int, input().split()))

    amount_per_spool = l // a
    spools_needed = math.ceil(q / amount_per_spool)
    total += spools_needed
    sub_total += spools_needed * l - a * q

print(total, sub_total)