import math

reds, yellows = [], []
for _ in range(10):
    red_pos = []
    red_data = list(map(int, input().split()))
    n = red_data[0]
    for idx in range(1, n * 2 + 1, 2):
        red_pos.append(("r", abs(red_data[idx] - 144), abs(red_data[idx + 1] - 84)))

    yellow_pos = []
    yellow_data = list(map(int, input().split()))
    n = yellow_data[0]
    for idx in range(1, n * 2 + 1, 2):
        yellow_pos.append(("y", abs(yellow_data[idx] - 144), abs(yellow_data[idx + 1] - 84)))

    reds.append(red_pos)
    yellows.append(yellow_pos)

red_count = 0
yellow_count = 0
for i in range(10):
    arr = []
    arr += reds[i]
    arr += yellows[i]
    arr.sort(key=lambda x: math.sqrt(x[1] ** 2 + x[2] ** 2))

    start = -1
    if len(arr) > 0:
        start = arr[0][0]
    idx = 0
    count = 0
    while idx < (len(reds[i]) + len(yellows[i])):
        if arr[idx][0] != start:
            break
        count += 1
        idx += 1

    if start == "r":
        red_count += count
    else:
        yellow_count += count

print(red_count, yellow_count)