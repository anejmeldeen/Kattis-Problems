n = int(input())
n *= 2

bit = [0] * (n + 1)
def add(idx, val):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx
def query(idx):
    total = 0
    while idx > 0:
        total += bit[idx]
        idx -= idx & -idx
    return total

person_to_time = {}
location_to_time = {}
total = 0
for time in range(1, n + 1):
    person, location = list(map(int, input().split()))
    if location in location_to_time:
        total += query(location_to_time[location])
    if person in person_to_time:
        add(person_to_time[person], -1)
    else:
        add(time, 1)
        person_to_time[person] = time
    location_to_time[location] = time

print(total)