nt, ns, rmax = list(map(int, input().split()))

tree_locs = []
for _ in range(nt):
    tree_locs.append(tuple(map(int, input().split())))

readings = []
for _ in range(ns):
    readings.append(list(map(int, input().split())))

pos_pos = set()
pos_neg = set()
neg_pos = set()
neg_neg = set()

tree_set = set(tree_locs)

x_dist, y_dist = readings[0]
for tree_x, tree_y in tree_locs:
    pos_pos.add((tree_x + x_dist, tree_y + y_dist))
    pos_neg.add((tree_x + y_dist, tree_y - x_dist))
    neg_pos.add((tree_x - x_dist, tree_y - y_dist))
    neg_neg.add((tree_x - y_dist, tree_y + x_dist))

for x_dist, y_dist in readings[1:]:
    n_pos_pos = set()
    n_pos_neg = set()
    n_neg_pos = set()
    n_neg_neg = set()

    for x, y in pos_pos:
        if (x - x_dist, y - y_dist) in tree_set:
            if (x, y) not in tree_set:
                n_pos_pos.add((x, y))
    for x, y in pos_neg:
        if (x - y_dist, y + x_dist) in tree_set:
            if (x, y) not in tree_set:
                n_pos_neg.add((x, y))
    for x, y in neg_pos:
        if (x + x_dist, y + y_dist) in tree_set:
            if (x, y) not in tree_set:
                n_neg_pos.add((x, y))
    for x, y in neg_neg:
        if (x + y_dist, y - x_dist) in tree_set:
            if (x, y) not in tree_set:
                n_neg_neg.add((x, y))

    pos_pos = n_pos_pos
    pos_neg = n_pos_neg
    neg_pos = n_neg_pos
    neg_neg = n_neg_neg

total = list(pos_pos) + list(pos_neg) + list(neg_pos) + list(neg_neg)
final = []

for x, y in total:
    count = 0
    for tree_x, tree_y in tree_set:
        if abs(tree_x - x) + abs(tree_y - y) <= rmax:
            count += 1

    if count == ns:
        final.append((x, y))

if len(final) == 1:
    x, y = final.pop()
    print(x, y)
elif len(final) > 1:
    print("Ambiguous")
else:
    print("Impossible")