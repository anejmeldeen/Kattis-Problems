data = list(map(int, input().split()))
jim_stats = []

for i in range(0, len(data), 2):
    jim_stats.append((data[i], data[i + 1]))

machine_stats = []
next_usage = {}
for i in range(10):
    data = list(map(int, input().split()))
    machine_stats.append((data[0], data[1]))
    next_usage[i] = data[2]

time = 0
for _ in range(3):
    for i in range(10):
        if time < next_usage[i]:
            next_usage[i] = max(next_usage[i], time + jim_stats[i][0])
            time += jim_stats[i][0] + jim_stats[i][1]
        else:
            diff = time - next_usage[i]
            remove = diff // (machine_stats[i][0] + machine_stats[i][1])
            next_usage[i] += remove * (machine_stats[i][0] + machine_stats[i][1])

            time = max(time, next_usage[i] + machine_stats[i][0]) + jim_stats[i][0]
            next_usage[i] = max(next_usage[i] + machine_stats[i][0] + machine_stats[i][1], time)
            time += jim_stats[i][1]

print(time - jim_stats[-1][-1])