n, q = list(map(int, input().split()))
locations = {}

arr = list(map(int, input().split()))
for i in range(n):
    locations[i + 1] = arr[i]

for _ in range(q):
    query = input().split()
    if query[0] == "1":
        locations[int(query[1])] = int(query[2])
    else:
        first = int(query[1])
        second = int(query[2])
        print(abs(locations[first] - locations[second]))