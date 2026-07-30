l, w = list(map(int, input().split()))

lanes = []
for _ in range(l):
    lanes.append(list(map(int, input().split())))
lanes.reverse()

pos, moves = input().split()
pos = int(pos)

safe = True
time = 0
lane_idx = -1
for char in moves:
    time += 1

    if char == "U":
        lane_idx += 1
    elif char == "D":
        lane_idx -= 1
    elif char == "L":
        pos -= 1
    elif char == "R":
        pos += 1

    if lane_idx < 0 or lane_idx >= l:
        continue

    o, i, s = lanes[lane_idx]

    if (lane_idx - l) % 2 == 1:
        car_loc = (o + time * s) % i
        bad = set()
        for ele in range(car_loc, car_loc - max(1, s), -1):
            bad.add(ele % i)
        new_pos = pos % i
        if new_pos in bad:
            safe = False
    else:
        car_loc = (o + time * s) % i
        bad = set()
        for ele in range(car_loc, car_loc - max(1, s), -1):
            bad.add(ele % i)
        new_pos = (w - pos - 1) % i
        if new_pos in bad:
            safe = False

print("safe" if safe and lane_idx >= l else "squish")