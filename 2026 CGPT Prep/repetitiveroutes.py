n = int(input())

class Fenwick:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

fenwick = Fenwick(2 * n)

person_seen_at = {}
location_last_seen_at = {}
total = 0

for time in range(1, 2 * n + 1):
    person, location = list(map(int, input().split()))

    if location in location_last_seen_at:
        total += fenwick.query(location_last_seen_at[location])
    location_last_seen_at[location] = time

    if person in person_seen_at:
        fenwick.add(person_seen_at[person], -1)
    else:
        fenwick.add(time, 1)
        person_seen_at[person] = time

print(total)