n, m = list(map(int, input().split()))
pieces = []
taken = set()

translate = {e: i + 1 for i, e in enumerate("ABCDEFGH")}

for _ in range(m):
    piece_type, loc = input().split()
    y_loc = int(loc[1])
    x_loc = translate[loc[0]]
    pieces.append((x_loc, y_loc, piece_type, loc))
    taken.add((x_loc, y_loc))

def nothing_in_between_horizontal(x1, x2, y, taken):
    x_diff = 1 if x2 - x1 > 0 else -1
    for i in range(x1 + x_diff, x2, x_diff):
        if (y, i) in taken:
            return False
    return True

def nothing_in_between_vertical(y1, y2, x, taken):
    y_diff = 1 if y2 - y1 > 0 else -1
    for i in range(y1 + y_diff, y2, y_diff):
        if (i, x) in taken:
            return False
    return True

def nothing_in_between_pos(x1, x2, y1, y2, taken):
    if x2 < x1:
        x1, y1, x2, y2 = x2, y2, x1, y1
    for diff in range(1, x2 - x1):
        if (x1 + diff, y1 + diff) in taken:
            return False
    return True

def nothing_in_between_neg(x1, x2, y1, y2, taken):
    if x2 < x1:
        x1, y1, x2, y2 = x2, y2, x1, y1
    for diff in range(1, x2 - x1):
        if (x1 - diff, y1 + diff) in taken:
            return False
    return True

def recurse(pieces, taken, path):
    if len(pieces) == 1:
        for row in path:
            print(row)
        exit()
    moves = []
    for i in range(len(pieces)):
        for j in range(len(pieces)):
            if i == j:
                continue
            piece_i_x, piece_i_y, piece_type, piece_i_loc = pieces[i]
            piece_j_x, piece_j_y, _, piece_j_loc = pieces[j]

            can_kill = False

            if piece_type == "N":
                x_dist = abs(piece_i_x - piece_j_x)
                y_dist = abs(piece_i_y - piece_j_y)
                if (x_dist == 1 and y_dist == 2) or (x_dist == 2 and y_dist == 1):
                    can_kill = True
            elif piece_type == "B":
                if piece_i_x + piece_i_y == piece_j_x + piece_j_y:
                    if nothing_in_between_neg(piece_i_x, piece_j_x, piece_i_y, piece_j_y, taken):
                        can_kill = True
                if piece_i_x - piece_i_y == piece_j_x - piece_j_y:
                    if nothing_in_between_pos(piece_i_x, piece_j_x, piece_i_y, piece_j_y, taken):
                        can_kill = True
            elif piece_type == "R":
                if piece_i_x == piece_j_x:
                    if nothing_in_between_horizontal(piece_i_y, piece_j_y, piece_i_x, taken):
                        can_kill = True
                if piece_i_y == piece_j_y:
                    if nothing_in_between_vertical(piece_i_x, piece_j_x, piece_i_y, taken):
                        can_kill = True
            elif piece_type == "Q":
                if piece_i_x + piece_i_y == piece_j_x + piece_j_y:
                    if nothing_in_between_neg(piece_i_x, piece_j_x, piece_i_y, piece_j_y, taken):
                        can_kill = True
                if piece_i_x - piece_i_y == piece_j_x - piece_j_y:
                    if nothing_in_between_pos(piece_i_x, piece_j_x, piece_i_y, piece_j_y, taken):
                        can_kill = True
                if piece_i_x == piece_j_x:
                    if nothing_in_between_horizontal(piece_i_y, piece_j_y, piece_i_x, taken):
                        can_kill = True
                if piece_i_y == piece_j_y:
                    if nothing_in_between_vertical(piece_i_x, piece_j_x, piece_i_y, taken):
                        can_kill = True
            elif piece_type == "K":
                if abs(piece_i_x - piece_j_x) <= 1 and abs(piece_i_y - piece_j_y) <= 1:
                    can_kill = True

            if can_kill:
                moves.append((piece_i_loc, piece_j_loc, piece_type, i, j))

    moves.sort()
    for move in moves:
        first_loc, second_loc, piece_type, i, j = move
        path.append(f"{piece_type}: {first_loc} -> {second_loc}")

        new_pieces = []
        new_taken = set()
        for k in range(len(pieces)):
            if k != i and k != j:
                new_pieces.append(pieces[k])
                new_taken.add((pieces[k][0], pieces[k][1]))
            if k == i:
                new_pieces.append((pieces[j][0], pieces[j][1], piece_type, second_loc))
                new_taken.add((pieces[j][0], pieces[j][1]))
        recurse(new_pieces, new_taken, path)

        path.pop()

recurse(pieces, taken, [])
print("No solution")