n = int(input())
events = []
for _ in range(n):
    event = input().split()
    s, c, g = list(map(int, event[1:]))
    if event[0] == "MISS":
        c, g = -c, -g
    events.append((s, c, g))

k = int(input())
events.sort(reverse=True)
idx = 0
while idx < len(events) and events[idx][0] > k:
    idx += 1

cheese = glory = 0
for i in range(idx, len(events)):
    cheese += events[i][1]
    glory += events[i][2]

print(cheese, glory)