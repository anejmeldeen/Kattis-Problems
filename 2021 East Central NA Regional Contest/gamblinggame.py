import math

n, num_squares, p = list(map(int, input().split()))

if p < num_squares:
    print("0/1")
    exit()

if num_squares == 0 and p == 0:
    print("1/1")
    exit()

incorrect = n - num_squares * 2
num_inc = p - num_squares

total_count = 0
for double_counts in range(num_squares):
    count = 0
    if incorrect >= (num_inc - double_counts) >= 0: 
        count = num_squares
        count *= math.comb(num_squares - 1, double_counts)
        count *= 2 ** (num_squares - 1 - double_counts)
        count *= math.comb(incorrect, num_inc - double_counts)

    total_count += count

total_count *= 2

total_ways = math.comb(n, p - 1) * (n - p + 1)

g = math.gcd(total_count, total_ways)
num = total_count // g
denom = total_ways // g

print(f"{num}/{denom}")