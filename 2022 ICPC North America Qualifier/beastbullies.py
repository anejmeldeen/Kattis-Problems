n = int(input())
strengths = []

for _ in range(n):
    strengths.append(int(input()))

strengths.sort()

curr = 0
count = 1
curr_count = 0
need = strengths[-1]
for i in range(n - 2, -1, -1):
    curr += strengths[i]
    curr_count += 1
    if curr >= need:
        count += curr_count
        need += curr
        curr_count = 0
        curr = 0

print(count)