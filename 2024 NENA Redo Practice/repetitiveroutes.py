n = int(input())

class FenwickTree:
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

tree = FenwickTree(2 * n)
person_to_time = {}
location_to_time = {}
cost = 0
for time in range(1, 2 * n + 1):
    person, location = list(map(int, input().split()))

    if location in location_to_time:
            cost += tree.query(location_to_time[location])
    location_to_time[location] = time
    
    if person not in person_to_time:
        person_to_time[person] = time
        tree.add(time, 1)
    else:
        tree.add(person_to_time[person], -1)

print(cost)