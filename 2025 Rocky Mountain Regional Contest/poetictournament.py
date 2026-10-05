import heapq

class Player:
    def __init__(self, id):
        self.id = id
        self.defeated = []

    def __lt__(self, other):
        print(f"? {self.id} {other.id}", flush=True)
        winner = int(input())
        return winner == self.id

n, k = list(map(int, input().split()))

sol = []
arr = [Player(i) for i in range(1, n + 1)]

while len(arr) > 1:
    next_arr = []
    for i in range(0, len(arr), 2):
        if i == len(arr) - 1:
            next_arr.append(arr[i])
            continue
        player_1 = arr[i]
        player_2 = arr[i + 1]
        print(f"? {player_1.id} {player_2.id}", flush=True)
        winner_id = int(input())

        if winner_id == player_1.id:
            next_arr.append(player_1)
            player_1.defeated.append(player_2)
        else:
            next_arr.append(player_2)
            player_2.defeated.append(player_1)
    arr = next_arr

sol.append(arr[0].id)
heap = []

for item in arr[0].defeated:
    heap.append(item)
heapq.heapify(heap)

for _ in range(k - 1):
    next_winner = heapq.heappop(heap)
    sol.append(next_winner.id)
    for add_me in next_winner.defeated:
        heapq.heappush(heap, add_me)

final = ["!"]
for item in sol:
    final.append(item)

print(' '.join(list(map(str, final))))