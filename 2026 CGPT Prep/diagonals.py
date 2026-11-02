n = int(input())


class Intersect:
    def __init__(self, val, i, j):
        count = (i == 0) + (j == 0) + (i == n) + (j == n)

        if count == 0:
            self.rem = 4
        elif count == 1:
            self.rem = 2
        else:
            self.rem = 1

        self.is_empty = val == "+"
        self.target = 0 if self.is_empty else int(val)
        self.curr = 0


board = []
for i in range(n + 1):
    row = input()
    board.append([
        Intersect(char, i, j)
        for j, char in enumerate(row)
    ])

sol = [["/"] * n for _ in range(n)]
used = [[False] * n for _ in range(n)]

parent = list(range((n + 1) ** 2))
size = [1] * ((n + 1) ** 2)


def find(a):
    while parent[a] != a:
        a = parent[a]
    return a


def endpoints(x, y, slash):
    if slash:
        return (
            (x + 1) * (n + 1) + y,
            x * (n + 1) + y + 1,
        )

    return (
        x * (n + 1) + y,
        (x + 1) * (n + 1) + y + 1,
    )


def can_place(x, y, slash):
    corners = (
        (x, y, not slash),
        (x, y + 1, slash),
        (x + 1, y, slash),
        (x + 1, y + 1, not slash),
    )

    for r, c, touches in corners:
        inter = board[r][c]
        if inter.is_empty:
            continue

        new_curr = inter.curr + touches
        new_rem = inter.rem - 1

        if not new_curr <= inter.target <= new_curr + new_rem:
            return False

    a, b = endpoints(x, y, slash)
    return find(a) != find(b)


def recurse(filled):
    if filled == n * n:
        for row in sol:
            print("".join(row))
        return True

    x = y = -1
    options = ()
    found_forced = False

    for i in range(n):
        for j in range(n):
            if used[i][j]:
                continue

            forward = can_place(i, j, True)
            backward = can_place(i, j, False)

            if not forward and not backward:
                return False

            if x == -1:
                x, y = i, j
                options = (forward, backward)

            if forward != backward:
                x, y = i, j
                options = (forward, backward)
                found_forced = True
                break

        if found_forced:
            break

    used[x][y] = True

    for slash, allowed in zip((True, False), options):
        if not allowed:
            continue

        a, b = endpoints(x, y, slash)
        root_a, root_b = find(a), find(b)

        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]

        sol[x][y] = "/" if slash else "\\"

        if slash:
            board[x][y + 1].curr += 1
            board[x + 1][y].curr += 1
        else:
            board[x][y].curr += 1
            board[x + 1][y + 1].curr += 1

        board[x][y].rem -= 1
        board[x][y + 1].rem -= 1
        board[x + 1][y].rem -= 1
        board[x + 1][y + 1].rem -= 1

        if recurse(filled + 1):
            return True

        if slash:
            board[x][y + 1].curr -= 1
            board[x + 1][y].curr -= 1
        else:
            board[x][y].curr -= 1
            board[x + 1][y + 1].curr -= 1

        board[x][y].rem += 1
        board[x][y + 1].rem += 1
        board[x + 1][y].rem += 1
        board[x + 1][y + 1].rem += 1

        size[root_a] -= size[root_b]
        parent[root_b] = root_b

    used[x][y] = False
    return False

recurse(0)