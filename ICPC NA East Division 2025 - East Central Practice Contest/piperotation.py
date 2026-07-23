n, m = list(map(int, input().split()))
board = [[("A", -1)] * (m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    chars = input()
    for j in range(1, m + 1):
        board[i][j] = (chars[j - 1], -1)

def connects(i, j, direc):
    if direc == "up":
        other_piece = board[i - 1][j]
        piece_type = other_piece[0]
        if piece_type == "A":
            return False
        if piece_type == "D":
            return True
        if piece_type == "C":
            return (other_piece[1] == 2 or other_piece[1] == 3)
        if piece_type == "B":
            return other_piece[1] == 0
        
    elif direc == "left":
        other_piece = board[i][j - 1]
        piece_type = other_piece[0]
        if piece_type == "A":
            return False
        if piece_type == "D":
            return True
        if piece_type == "C":
            return (other_piece[1] == 2 or other_piece[1] == 1)
        if piece_type == "B":
            return other_piece[1] == 1
        

possible = True
for i in range(1, n + 2):
    for j in range(1, m + 2):
        piece = board[i][j]
        connects_up = connects(i, j, "up")
        connects_left = connects(i, j, "left")
        if piece[0] == "A":
            if connects_up or connects_left:
                possible = False
                break
            board[i][j] = ("A", 0)
        elif piece[0] == "D":
            if not connects_up or not connects_left:
                possible = False
                break
            board[i][j] = ("D", 0)
        elif piece[0] == "C":
            if connects_up and connects_left:
                board[i][j] = ("C", 0)
            elif connects_up:
                board[i][j] = ("C", 1)
            elif connects_left:
                board[i][j] = ("C", 3)
            else:
                board[i][j] = ("C", 2)
        elif piece[0] == "B":
            if (connects_up and connects_left) or (not connects_up and not connects_left):
                possible = False
                break
            elif connects_up:
                board[i][j] = ("B", 0)
            else:
                board[i][j] = ("B", 1)

if possible:
    print("Possible")
else:
    print("Impossible")