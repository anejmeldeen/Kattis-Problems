from collections import defaultdict

t, p = list(map(int, input().split()))

relationships = defaultdict(list)

all_names = set()
bad_names = set()

for _ in range(t):
    data = input().split()
    names = data[2:]

    for i in range(len(data)):
        if i == 1:
            continue
        all_names.add(data[i])

    for name in names:
        bad_names.add(name)
        relationships[data[0]].append(name)

my_parents = defaultdict(set)

def recurse(curr, add):
    my_parents[curr].add(add)
    for conn in relationships[curr]:
        recurse(conn, add)

for name in all_names:
    recurse(name, name)

root = all_names.difference(bad_names).pop()

def dist_finder(at, looking_for):
    if at == looking_for:
        return 0
    best = float('inf')
    for conn in relationships[at]:
        best = min(best, dist_finder(conn, looking_for))
    return 1 + best

for _ in range(p):
    a, b = input().split()

    curr = root
    change = True
    while change:
        change = False
        for child in relationships[curr]:
            if child in my_parents[a] and child in my_parents[b]:
                curr = child
                change = True
                break

    a_dist = dist_finder(curr, a)
    b_dist = dist_finder(curr, b)

    if b_dist == 0:
        a_dist, b_dist = b_dist, a_dist
        a, b = b, a

    if a_dist == b_dist:
        if a_dist == 1:
            print(f"{a} and {b} are siblings")
        else:
            number = str(a_dist - 1)
            if len(number) >= 2 and number[-2] == "1":
                add = "th"
            elif number[-1] == "1":
                add = "st"
            elif number[-1] == "2":
                add = "nd"
            elif number[-1] == "3":
                add = "rd"
            else:
                add = "th"
            print(f"{a} and {b} are {number}{add} cousins")
    elif a_dist == 0:
        if b_dist == 1:
            print(f"{b} is the child of {a}")
        else:
            greats = "great " * (b_dist - 2)
            print(f"{b} is the {greats}grandchild of {a}")
    else:
        times = abs(a_dist - b_dist)
        number = str(min(a_dist, b_dist) - 1)
        if times > 1:
            s = "s"
        else:
            s = ""
        if len(number) >= 2 and number[-2] == "1":
            add = "th"
        elif number[-1] == "1":
            add = "st"
        elif number[-1] == "2":
            add = "nd"
        elif number[-1] == "3":
            add = "rd"
        else:
            add = "th"
        print(f"{a} and {b} are {number}{add} cousins, {times} time{s} removed")