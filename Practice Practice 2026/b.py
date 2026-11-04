import heapq

n, k = list(map(int, input().split()))
times = list(map(int, input().split()))
times.sort()

heap = [0] * k

total = 0
for time in times:
    lowest = heapq.heappop(heap)
    new = lowest + time
    total += new
    heapq.heappush(heap, new)

print(total)