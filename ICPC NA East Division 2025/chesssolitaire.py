n, m = list(map(int, input().split()))
pieces = []

letter_to_num = {e: i for i, e in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
x_to_str = {i: e for i, e in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

loc_to_piece = {}
for _ in range(m):
    data = input().split()
    piece_type = data[0]
    x = letter_to_num[data[1][0]]
    y = int(data[1][1]) - 1
    loc_to_piece[(x, y)] = piece_type

def recurse(loc_to_piece):
    valid_moves = []
    for curr_loc in loc_to_piece:
        for new_loc in loc_to_piece:
            if curr_loc == new_loc:
                continue
            allowed = False
            if loc_to_piece[curr_loc] == "N":
                x_diff = abs(curr_loc[0] - new_loc[0])
                y_diff = abs(curr_loc[1] - new_loc[1])
                if (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2):
                    allowed = True
            elif loc_to_piece[curr_loc] == "Q":
                if ((curr_loc[0] + curr_loc[1]) == (new_loc[0] + new_loc[1])) or ((curr_loc[0] - curr_loc[1]) == (new_loc[0] - new_loc[1])):
                    allowed = True
                if (curr_loc[0] == new_loc[0]) or (curr_loc[1] == new_loc[1]):
                    allowed = True
                    if new_loc[0] > curr_loc[0]:
                        x_shift = 1
                    elif new_loc[0] == curr_loc[0]:
                        x_shift = 0
                    else:
                        x_shift = -1
                    if new_loc[1] > curr_loc[1]:
                        y_shift = 1
                    elif new_loc[1] == curr_loc[1]:
                        y_shift = 0
                    else:
                        y_shift = -1
                    for mult in range(1, max(abs(new_loc[0] - curr_loc[0]), abs(new_loc[1] - curr_loc[1]))):
                        if (curr_loc[0] + x_shift * mult, curr_loc[1] + y_shift * mult) in loc_to_piece:
                            allowed = False
            elif loc_to_piece[curr_loc] == "B":
                if ((curr_loc[0] + curr_loc[1]) == (new_loc[0] + new_loc[1])) or ((curr_loc[0] - curr_loc[1]) == (new_loc[0] - new_loc[1])):
                    allowed = True
                    if new_loc[0] > curr_loc[0]:
                        x_shift = 1
                    elif new_loc[0] == curr_loc[0]:
                        x_shift = 0
                    else:
                        x_shift = -1
                    if new_loc[1] > curr_loc[1]:
                        y_shift = 1
                    elif new_loc[1] == curr_loc[1]:
                        y_shift = 0
                    else:
                        y_shift = -1
                    for mult in range(1, max(abs(new_loc[0] - curr_loc[0]), abs(new_loc[1] - curr_loc[1]))):
                        if (curr_loc[0] + x_shift * mult, curr_loc[1] + y_shift * mult) in loc_to_piece:
                            allowed = False
            elif loc_to_piece[curr_loc] == "K":
                x_diff = abs(curr_loc[0] - new_loc[0])
                y_diff = abs(curr_loc[1] - new_loc[1])
                if x_diff <= 1 and y_diff <= 1:
                    allowed = True
            elif loc_to_piece[curr_loc] == "R":
                if (curr_loc[0] == new_loc[0]) or (curr_loc[1] == new_loc[1]):
                    allowed = True
                    if new_loc[0] > curr_loc[0]:
                        x_shift = 1
                    elif new_loc[0] == curr_loc[0]:
                        x_shift = 0
                    else:
                        x_shift = -1
                    if new_loc[1] > curr_loc[1]:
                        y_shift = 1
                    elif new_loc[1] == curr_loc[1]:
                        y_shift = 0
                    else:
                        y_shift = -1
                    for mult in range(1, max(abs(new_loc[0] - curr_loc[0]), abs(new_loc[1] - curr_loc[1]))):
                        if (curr_loc[0] + x_shift * mult, curr_loc[1] + y_shift * mult) in loc_to_piece:
                            allowed = False
            
            if allowed:
                valid_moves.append((curr_loc, new_loc))

    valid_moves.sort()
    for move in valid_moves:
        loc_to_piece_copy = loc_to_piece.copy()
        loc_to_piece_copy[move[1]] = loc_to_piece[move[0]]
        del loc_to_piece_copy[move[0]]

        curr_loc = x_to_str[move[0][0]] + str(move[0][1] + 1)
        new_loc = x_to_str[move[1][0]] + str(move[1][1] + 1)

        if len(loc_to_piece_copy) == 1:
            return (True, f"{loc_to_piece[move[0]]}: {curr_loc} -> {new_loc}")
        res = recurse(loc_to_piece_copy)
        if res[0]:
            return (True, f"{loc_to_piece[move[0]]}: {curr_loc} -> {new_loc}\n" + res[1])

    return (False, "")

res = recurse(loc_to_piece)

if res[0] == True:
    print(res[1])
else:
    print("No solution")