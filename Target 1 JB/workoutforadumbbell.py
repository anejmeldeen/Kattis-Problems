data = list(map(int, input().split()))
john_stats = []

for i in range(0, len(data), 2):
    john_stats.append((data[i], data[i + 1]))

machine_stats = []
next_use_time = []
for i in range(10):
    u, r, t = list(map(int, input().split()))
    machine_stats.append((u, r))
    next_use_time.append(t)

john_next_time = 0
for j in range(3):
    for i in range(10):
        if john_next_time >= next_use_time[i]:
            diff = john_next_time - next_use_time[i]
            shuffle = diff // (machine_stats[i][0] + machine_stats[i][1])
            next_use_time[i] += (machine_stats[i][0] + machine_stats[i][1]) * shuffle

            john_next_time = max(john_next_time, next_use_time[i] + machine_stats[i][0]) + john_stats[i][0] + john_stats[i][1]
            next_use_time[i] = max(next_use_time[i] + machine_stats[i][0] + machine_stats[i][1], john_next_time - john_stats[i][1])
        else:
            next_use_time[i] = max(next_use_time[i], john_next_time + john_stats[i][0])
            john_next_time += john_stats[i][0] + john_stats[i][1]

print(john_next_time - john_stats[-1][1])