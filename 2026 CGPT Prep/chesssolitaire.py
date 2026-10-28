n, m = list(map(int, input().split()))

letter_num = {e: i + 1 for i, e in enumerate("ABCDEFGHIJKLMNOP")}

pieces = []
for _ in range(m):
    piece_type, loc = input().split()
    x_loc = letter_num[loc[0]]
    y_loc = int(loc[1])
    pieces.append((x_loc, y_loc, piece_type, loc))

def recurse(pieces, print_me):
    if len(pieces) == 1:
        for row in print_me:
            print(row)
        exit()

    moves = []
    locations = set()
    for piece in pieces:
        locations.add((piece[0], piece[1]))

    for i in range(len(pieces)):
        for j in range(len(pieces)):
            if i == j:
                continue

            i_x, i_y, piece_i, loc_i = pieces[i]
            j_x, j_y, piece_j, loc_j = pieces[j]

            works = False

            if piece_i == "K":
                x_diff = abs(i_x - j_x)
                y_diff = abs(i_y - j_y)
                if x_diff <= 1 and y_diff <= 1:
                    works = True
            if piece_i == "N":
                x_diff = abs(i_x - j_x)
                y_diff = abs(i_y - j_y)
                if (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
                    works = True
            if piece_i == "Q" or piece_i == "R":
                if i_y == j_y:
                    can = True
                    mini = min(i_x, j_x)
                    maxi = max(i_x, j_x)
                    for k in range(mini + 1, maxi):
                        if (k, i_y) in locations:
                            can = False
                    if can:
                        works = True
                if i_x == j_x:
                    can = True
                    mini = min(i_y, j_y)
                    maxi = max(i_y, j_y)
                    for k in range(mini + 1, maxi):
                        if (i_x, k) in locations:
                            can = False
                    if can:
                        works = True
            if piece_i == "Q" or piece_i == "B":
                if (i_y - i_x) == (j_y - j_x):
                    can = True
                    if i_x > j_x:
                        i_x, j_x, i_y, j_y = j_x, i_x, j_y, i_y
                    for diff in range(1, j_x - i_x):
                        if (i_x + diff, i_y + diff) in locations:
                            can = False
                    if can:
                        works = True
                if (i_x + i_y) == (j_x + j_y):
                    can = True
                    if i_x > j_x:
                        i_x, j_x, i_y, j_y = j_x, i_x, j_y, i_y
                    for diff in range(1, j_x - i_x):
                        if (i_x + diff, i_y - diff) in locations:
                            can = False
                    if can:
                        works = True

            if works:
                moves.append((loc_i, loc_j, i, j, piece_i, j_x, j_y))

    moves.sort()
    for i in range(len(moves)):
        loc_i, loc_j, idx1, idx2, piece_i, j_x, j_y = moves[i]
        new_pieces = []
        for j in range(len(pieces)):
            if j == idx1 or j == idx2:
                continue
            new_pieces.append(pieces[j])
        new_pieces.append((pieces[idx2][0], pieces[idx2][1], piece_i, loc_j))
        print_me.append(f"{piece_i}: {loc_i} -> {loc_j}")
        recurse(new_pieces, print_me)
        print_me.pop()

recurse(pieces, [])
print("No solution")