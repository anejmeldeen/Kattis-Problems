from collections import defaultdict
from functools import cache

number = list(map(int, list(input())))
real_num = int(''.join(list(map(str, number))))
length = len(number)

@cache
def get_pows(n):
    pows = []
    curr = 1
    while curr < 10000000:
        pows.append(curr)
        curr *= n
    return pows

left_size = length // 2
right_size = length - left_size

def grab_counts(left, right):
    counts = defaultdict(int)
    counts[0] = 1

    for i in range(left, right):
        new_counts = defaultdict(int)
        for num in get_pows(number[i]):
            for key in counts:
                new_counts[key + num] += counts[key]
        counts = new_counts

    return counts

left_counts = grab_counts(0, left_size)
right_counts = grab_counts(left_size, left_size + right_size)

sol = 0
for key in left_counts:
    need = real_num - key
    sol += left_counts[key] * right_counts[need]
print(sol)