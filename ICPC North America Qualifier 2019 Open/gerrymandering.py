p, d = list(map(int, input().split()))
counts = {}

for _ in range(p):
    data = list(map(int, input().split()))
    district = data[0]

    if district not in counts:
        counts[district] = [0, 0]
    counts[district][0] += data[1]
    counts[district][1] += data[2]

total_votes = 0
total_a_count = 0
total_b_count = 0
for district in range(1, d + 1):
    a_count, b_count = counts[district]
    need = (a_count + b_count) // 2 + 1

    if a_count > b_count:
        print(f"A {a_count - need} {b_count}")
        total_a_count += a_count - need
        total_b_count += b_count
    else:
        print(f"B {a_count} {b_count - need}")
        total_a_count += a_count
        total_b_count += b_count - need

    total_votes += a_count + b_count

print(abs(total_a_count - total_b_count) / total_votes)