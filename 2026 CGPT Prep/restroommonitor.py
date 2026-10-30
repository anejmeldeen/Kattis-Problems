import heapq

s, n = list(map(int, input().split()))

people = []
toilet = []
for _ in range(n):
    data = input().split()
    people.append(int(data[0]))
    if data[1] == "y":
        toilet.append(int(data[0]))

people.sort()
toilet.sort()

heap = [0] * s

for i in range(len(toilet)):
    if i + 1 > toilet[i]:
        print("No")
        exit()

for person in people:
    next_time = heapq.heappop(heap)
    if next_time + 1 > person:
        print("No")
        exit()
    heapq.heappush(heap, next_time + 1)

print("Yes")