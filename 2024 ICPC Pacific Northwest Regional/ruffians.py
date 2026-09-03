t = int(input())
for _ in range(t):
    found = False
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    board = [first, second]
    for i in range(2):
        for j in range(5):
            curr = board[i][j]
            for x in range(2):
                for y in range(5):
                    if x == i or y == j:
                        continue
                    if board[x][y] == board[i][j]:
                        found = True
    print("YES" if found else "NO")