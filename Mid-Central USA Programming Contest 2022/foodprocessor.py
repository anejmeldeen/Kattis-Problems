import math

s, t, n = list(map(int, input().split()))

blades = []
for _ in range(n):
    m, h = list(map(int, input().split()))
    blades.append((m, h))

blades.sort(key=lambda x: -x[0])
remove = []

new_blades = [blades[0]]
for i in range(n - 1):
    if blades[i + 1][1] > new_blades[-1][1] or blades[i + 1][0] < t:
        pass
    else:
        new_blades.append(blades[i + 1])
blades = new_blades

blades.append((t, 0))

if blades[0][0] < s:
    print(-1)
else:
    total_time = 0
    for i in range(len(blades) - 1):
        if s < blades[i + 1][0]:
            continue
        diff = s / blades[i + 1][0]
        log_diff = math.log(diff, 2)
        log_diff *= blades[i][1]
        total_time += log_diff
        s = blades[i + 1][0]
    print(total_time)