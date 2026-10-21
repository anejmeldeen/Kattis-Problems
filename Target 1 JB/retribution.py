n, m, p = list(map(int, input().split()))

judges = []
tars = []
feathers = []

total = 0

for _ in range(n):
    judges.append(tuple(map(int, input().split())))
for _ in range(m):
    tars.append(tuple(map(int, input().split())))
for _ in range(p):
    feathers.append(tuple(map(int, input().split())))

def fnc(judges, tars):
    global total

    seen_judges = set()
    seen_tars = set()
    arr = []
    for i, judge in enumerate(judges):
        for j, tar in enumerate(tars):
            judge_x, judge_y, tar_x, tar_y = judge[0], judge[1], tar[0], tar[1]
            dist = ((judge_x - tar_x) ** 2 + (judge_y - tar_y) ** 2) ** 0.5
            arr.append((dist, i, j))
    arr.sort(reverse=True)
    
    while len(seen_judges) < n:
        dist, judge_idx, tar_idx = arr.pop()

        if judge_idx in seen_judges or tar_idx in seen_tars:
            continue
        total += dist
        seen_judges.add(judge_idx)
        seen_tars.add(tar_idx)

fnc(judges, tars)
fnc(judges, feathers)

print(total)