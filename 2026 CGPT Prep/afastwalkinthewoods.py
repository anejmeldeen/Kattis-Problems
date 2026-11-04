from collections import defaultdict

n, m = list(map(int, input().split()))

class Intersection:
    def __init__(self):
        self.arr = [None, None, None, None]

    def __str__(self):
        return self.arr.__str__()

global_first = True

locations = []
data = list(map(int, input().split()))
for i in range(0, 2 * n, 2):
    locations.append((data[i], data[i + 1]))

graph = defaultdict(Intersection)
for _ in range(m):
    i, j, k = list(map(int, input().split()))

    loc_i = locations[i - 1]
    loc_j = locations[j - 1]

    if loc_i[0] > loc_j[0]:
        graph[j].arr[1] = [i, k]
        graph[i].arr[3] = [j, k]
    elif loc_i[0] < loc_j[0]:
        graph[i].arr[1] = [j, k]
        graph[j].arr[3] = [i, k]
    elif loc_j[1] > loc_i[1]:
        graph[i].arr[0] = [j, k]
        graph[j].arr[2] = [i, k]
    else:
        graph[i].arr[2] = [j, k]
        graph[j].arr[0] = [i, k]

start_loc, start_dir = input().split()
start_loc = int(start_loc)

dir_to_int = {e: i for i, e in enumerate("NESW")}
start_dir = dir_to_int[start_dir]
loc, curr_dir = start_loc, start_dir

while True:
    path = []
    seen = {}
    i = 0
    skip_later = False
    while True:
        if (loc, curr_dir) in seen:
            break
        seen[(loc, curr_dir)] = i
        i += 1
        if global_first:
            paths = [(graph[loc].arr[curr_dir], 0)]
            global_first = False
        else:
            paths = [x for x in [(graph[loc].arr[(curr_dir - 1) % 4], -1), (graph[loc].arr[curr_dir], 0), (graph[loc].arr[(curr_dir + 1) % 4], 1)] if x[0]]
        if len(paths) == 3:
            item = (loc, curr_dir)
            path.append(item)
            loc = paths[1][0][0]
        elif len(paths) > 0:
            item = (loc, (curr_dir + paths[0][1]) % 4)
            path.append(item)
            loc = paths[0][0][0]
            curr_dir = (curr_dir + paths[0][1]) % 4
        else:
            print(locations[loc - 1][0], locations[loc - 1][1])
            exit()

        graph[item[0]].arr[item[1]][1] -= 1
        new_loc = graph[item[0]].arr[item[1]][0]
        if graph[item[0]].arr[item[1]][1] == 0:
            graph[item[0]].arr[item[1]] = None

        new_dir = (item[1] + 2) % 4
        item = (new_loc, new_dir)

        graph[item[0]].arr[item[1]][1] -= 1
        if graph[item[0]].arr[item[1]][1] == 0:
            graph[item[0]].arr[item[1]] = None
            skip_later = True
            break

    if skip_later:
        continue

    path = path[seen[(loc, curr_dir)]:]
    min_weight = float('inf')

    edges = defaultdict(int)
    for item in path:
        loc1 = item[0]
        loc2 = graph[item[0]].arr[item[1]][0]
        value = graph[item[0]].arr[item[1]][1]

        if loc1 > loc2:
            loc1, loc2 = loc2, loc1

        edges[(loc1, loc2, value)] += 1

    for edge in edges:
        times_used = edges[edge]
        remaining = edge[2]
        min_weight = min(min_weight, remaining // times_used)
    for item in path:
        graph[item[0]].arr[item[1]][1] -= min_weight
        new_loc = graph[item[0]].arr[item[1]][0]
        if graph[item[0]].arr[item[1]][1] == 0:
            graph[item[0]].arr[item[1]] = None

        new_dir = (item[1] + 2) % 4
        item = (new_loc, new_dir)

        graph[item[0]].arr[item[1]][1] -= min_weight
        if graph[item[0]].arr[item[1]][1] == 0:
            graph[item[0]].arr[item[1]] = None