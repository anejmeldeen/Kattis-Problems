from collections import defaultdict, deque

n, m = list(map(int, input().split()))

x_map = defaultdict(list)
y_map = defaultdict(list)
x_map_rev = defaultdict(list)
y_map_rev = defaultdict(list)

spy_locs = []
for i in range(n):
    x, y = list(map(int, input().split()))
    x_map[x].append((y, i))
    y_map[y].append((x, i))
    x_map_rev[x].append((y, i))
    y_map_rev[y].append((x, i))
    spy_locs.append((x, y))

for key in x_map:
    x_map[key] = deque(sorted(x_map[key]))
for key in y_map:
    y_map[key] = deque(sorted(y_map[key]))

dead = set()
moves = []
for _ in range(m):
    team, direction = input().split()
    team = int(team) - 1

    if team in dead:
        print("ignore")
        continue

    x, y = spy_locs[team]
    sol = []
    if direction == "N":
        q = x_map[x]
        kill = []
        while q[-1][0] > y:
            kill.append(q.pop()[1])
    elif direction == "E":
        q = y_map[y]
        kill = []
        while q[-1][0] > x:
            kill.append(q.pop()[1])
    elif direction == "S":
        q = x_map[x]
        kill = []
        while q[0][0] < y:
            kill.append(q.popleft()[1])
    elif direction == "W":
        q = y_map[y]
        kill = []
        while q[0][0] < x:
            kill.append(q.popleft()[1])
    
    kill = kill[::-1]
    for ele in kill:
        if ele in dead:
            continue
        dead.add(ele)
        sol.append(ele)
    print(len(sol), ' '.join(list(map(lambda x: str(x + 1), sol))))