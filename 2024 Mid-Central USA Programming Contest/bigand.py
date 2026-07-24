import heapq

n, d, l = list(map(int, input().split()))
heap = list(map(int, input().split()))

heapq.heapify(heap)

while len(heap) > 1:
    lowest = heapq.heappop(heap)
    second = heapq.heappop(heap)
    heapq.heappush(heap, second + d)

print(heap[0] + l)