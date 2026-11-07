from functools import cache
import random

for n in range(100):
    for i in range(10):
        board = []
        for _ in range(n):
            choices = [random.randint(-10, -1), random.randint(1, 10)]
            board.append(random.choice(choices))

        cycle_len = {}

        def get_cycle_len(idx):
            seen = set()
            path = []
            while idx not in seen:
                seen.add(idx)
                path.append(idx)
                idx = idx + board[idx]
            return path

        seen = set()

        @cache
        def find_cycles(idx):
            if idx < 0 or idx >= n:
                return
            if idx in seen:
                if idx in cycle_len:
                    return
                path = get_cycle_len(idx)
                cycle_len[idx] = len(path)
                for idx in path:
                    cycle_len[idx] = len(path)

            seen.add(idx)
            find_cycles(idx + board[idx])

        @cache
        def solve(idx):
            if idx < 0 or idx >= n:
                return 0

            if idx in cycle_len:
                return cycle_len[idx]

            res = solve(idx + board[idx])
            return 1 + res

        for i in range(n):
            find_cycles(i)

        total = 0
        for i in range(n):
            total += solve(i)

        mine = 0
        for s in range(n):
            for m in range(n):
                m = board[m]
                seen = set()
                h = 0
                while True:
                    if board[s] == m:
                        mine += h
                        break
                    if s in seen:
                        mine += h
                        break
                    seen.add(s)

                    num = board[s]
                    s = s + num
                    h += 1
                    if s < 0:
                        mine += h
                        break
                    elif s >= n:
                        mine += h
                        break
        print(n, board, total, mine)