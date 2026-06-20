p = int(input())
for _ in range(p):
    k, n = list(map(int, input().split()))

    moves = []
    while n > 0:
        if n & 1:
            moves.append("r")
        else:
            moves.append("l")
        n >>= 1

    num = 1
    denom = 1

    for i in range(len(moves) - 2, -1, -1):
        if moves[i] == "l":
            denom += num
        else:
            num += denom

    print(f"{k} {num}/{denom}")