import math

n, m, s, p, q = list(map(int, input().split()))
num_pages = math.ceil(n / m)

pages = {}
for i in range(1, num_pages + 1):
    pages[i] = (set(), set())

for i in range(p + q):
    num = int(input())
    page_its_on = (num - 1) // m + 1

    if i < p:
        pages[page_its_on][0].add(num)
    else:
        pages[page_its_on][1].add(num)

lowest = float('inf')
highest = -float('inf')
for page in range(1, num_pages + 1):
    sets = pages[page]
    set_have = sets[0]
    set_need = sets[1]

    if (len(set_have) != len(set_need) or len(set_have) != len(set_have | set_need)):
        lowest = min(lowest, page)
        highest = max(highest, page)

solution = 0
if highest == -float('inf'):
    solution = 0
elif s >= highest:
    solution = s - lowest
elif s <= lowest:
    solution = highest - s
else:
    dist1 = s - lowest
    dist2 = highest - s
    mini = min(dist1, dist2)
    maxi = max(dist1, dist2)
    solution = 2 * mini + maxi

def solve(page_num):
    case1, case2, case3 = 0, 1, 1

    sets = pages[page_num]
    have = sets[0]
    need = sets[1]

    for num in have:
        if num not in need:
            case1 += 1
    for num in need:
        if num not in have:
            case1 += 1

    amount = m
    if page_num == num_pages:
        amount = (n - 1) % m + 1

    case2 += amount - len(need)

    case3 += len(need)

    return min(case1, case2, case3)

for page_num in range(1, num_pages + 1):
    solution += solve(page_num)

print(solution)