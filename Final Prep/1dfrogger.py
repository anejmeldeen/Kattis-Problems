n, s, m = list(map(int, input().split()))
board = list(map(int, input().split()))

s -= 1

for s in range(n):
    for m in range(n):
        m = board[m]
        seen = set()
        h = 0
        while True:
            if board[s] == m:
                print("magic")
                print(h)
                break
            if s in seen:
                print("cycle")
                print(h)
                break
            seen.add(s)

            num = board[s]
            s = s + num
            h += 1
            if s < 0:
                print("left")
                print(h)
                break
            elif s >= n:
                print("right")
                print(h)
                break