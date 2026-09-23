from functools import cache

while (data := input()) != "0 0":
    n, k = list(map(int, data.split()))
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    @cache
    def recurse(idx, k_left, last):
        if k_left < 0:
            return -float('inf')
        if idx == n:
            if k_left == 0:
                return 0
            else:
                return -float('inf')
        zero_poss = True
        one_poss = last in [0, 1]
        two_poss = last in [0, 2]

        best = float('-inf')
        if zero_poss:
            curr = sum(board[idx])
            curr += recurse(idx + 1, k_left, 0)
            best = max(best, curr)
        if one_poss:
            curr = board[idx][0]
            curr += recurse(idx + 1, k_left - 1, 1)
            best = max(best, curr)
        if two_poss:
            curr = board[idx][1]
            curr += recurse(idx + 1, k_left - 1, 2)
            best = max(best, curr)
        return best

    print(recurse(0, k, 0))