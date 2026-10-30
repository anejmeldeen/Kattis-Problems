from functools import cache

while (data := input()) != "0 0":
    n, k = list(map(int, data.split()))
    board = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    @cache
    def recurse(idx, last, k):
        if idx == n:
            if k == 0:
                return 0
            return float('-inf')

        if k < 0:
            return float('-inf')

        best = float('-inf')
        best = max(best, board[idx][0] + board[idx][1] + recurse(idx + 1, 0, k))

        if last != 2:
            best = max(best, board[idx][0] + recurse(idx + 1, 1, k - 1))

        if last != 1:
            best = max(best, board[idx][1] + recurse(idx + 1, 2, k - 1))

        return best

    print(recurse(0, 0, k))