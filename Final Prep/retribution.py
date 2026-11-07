n, m, p = list(map(int, input().split()))

judges = []
tars = []
feathers = []

for _ in range(n):
    judges.append(list(map(int, input().split())))
for _ in range(m):
    tars.append(list(map(int, input().split())))
for _ in range(p):
    feathers.append(list(map(int, input().split())))

judge_tar = []
judge_feather = []
for i, judge in enumerate(judges):
    for j, tar in enumerate(tars):
        dist = ((judge[0] - tar[0]) ** 2 + (judge[1] - tar[1]) ** 2)
        judge_tar.append((dist, i, j))
    for j, feather in enumerate(feathers):
        dist = ((judge[0] - feather[0]) ** 2 + (judge[1] - feather[1]) ** 2)
        judge_feather.append((dist, i, j))

judge_tar.sort()
judge_feather.sort()

count = 0
tar_seen = set()
feather_seen = set()
tar_tar_seen = set()
feather_feather_seen = set()
for item in judge_tar:
    if item[1] not in tar_seen and item[2] not in tar_tar_seen:
        count += item[0] ** 0.5
        tar_seen.add(item[1])
        tar_tar_seen.add(item[2])
    if len(tar_seen) == n:
        break
for item in judge_feather:
    if item[1] not in feather_seen and item[2] not in feather_feather_seen:
        count += item[0] ** 0.5
        feather_seen.add(item[1])
        feather_feather_seen.add(item[2])
    if len(feather_seen) == n:
        break
print(count)