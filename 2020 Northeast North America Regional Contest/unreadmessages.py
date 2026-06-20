n, m = list(map(int, input().split()))
messages = []

for _ in range(m):
    messages.append(int(input()))

last_sent = {}

total = 0
curr_time = 0
for message in messages:
    total += n
    curr_time += 1

    if message in last_sent:
        total -= curr_time - last_sent[message]
    else:
        total -= curr_time
    last_sent[message] = curr_time

    print(total)