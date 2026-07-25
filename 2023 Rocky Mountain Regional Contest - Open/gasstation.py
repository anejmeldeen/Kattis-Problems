from collections import deque

p, n = list(map(int, input().split()))
car_queue = deque()
sol = [0] * n

pumps = [[0, 0] for _ in range(2 * p)]
pump_queues = [deque() for _ in range(2 * p)]

for i in range(n):
    data = input().split()
    car_queue.append([int(data[0]), int(data[1]), data[2], i])

for time in range(10 ** 5 + 101):
    for pump in pumps:
        for i, car in enumerate(pump):
            if car == 0:
                continue
            if car[0] + car[1] == time:
                sol[car[3]] = time
                pump[i] = 0

    # move queues as much as possible
    for i in range(2 * p):
        queue = pump_queues[i]
        pump = pumps[i]
        if pump[0] == 0 and pump[1] == 0:
            if len(queue) > 0:
                car = queue.popleft()
                car[0] = time
                pump[1] = car
            if len(queue) > 0:
                car = queue.popleft()
                car[0] = time
                pump[0] = car
        elif pump[0] == 0:
            if len(queue) > 0:
                car = queue.popleft()
                car[0] = time
                pump[0] = car

    if car_queue and car_queue[0][0] == time:
        car = car_queue.popleft()
        direction = car[2]
        low_bound = 0
        if direction == "L":
            low_bound = 1

        # find open lane
        found_open_lane = False
        for i in range(low_bound, p * 2, 2):
            pump = pumps[i]
            if pump[0] != 0:
                continue
            if pump[1] == 0:
                pump[1] = car
            else:
                pump[0] = car
            found_open_lane = True
            break

        # find shortest queue if not found open lane
        if not found_open_lane:
            shortest_queue = float('inf')
            pump_to_queue_at = -1
            for i in range(low_bound, p * 2, 2):
                if len(pump_queues[i]) < shortest_queue:
                    shortest_queue = len(pump_queues[i])
                    pump_to_queue_at = pump_queues[i]
            pump_to_queue_at.append(car)

for num in sol:
    print(num)