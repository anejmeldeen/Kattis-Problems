import sys
data = sys.stdin.readlines()

tf = float(data[0])
tr = float(data[1])
speeds = [float(x) for x in data[2:]]

last_acc_speed = 0

for idx, speed in enumerate(speeds):
    if 0 < speed < 1:
        print(1)
        continue

    if speed % 1 == 0:
        print(int(speed))
        continue

    integer = int(speed)
    low_bound = integer + tf
    high_bound = integer + tr

    if speed < low_bound:
        print(integer)
        continue
    if speed > high_bound:
        print(integer + 1)
        continue

    use_me = -1
    for i in range(idx - 1, -1, -1):
        if speeds[i] < low_bound or speeds[i] > high_bound:
            use_me = speeds[i]
            break

    if use_me < high_bound:
        print(integer)
    else:
        print(integer + 1)