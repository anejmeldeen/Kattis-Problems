import random

def query(x, y):
    print(f"{x} {y}", flush=True)
    res = input()
    return (res == "T")

def solve():
    x = random.choice([-1, 1])
    y = random.choice([-2, 2])

    first, second = -1, -1

    if not query(x, y):
        first, second = False, False
    elif not query(-x, y):
        first, second = True, False
    elif not query(x, -y):
        first, second = False, True
    else:
        first, second = True, True

    if x < 0:
        first = not first
    if y < 0:
        second = not second

    return first, second

t = int(input())
for _ in range(t):
    n = int(input())

    choice1 = 1
    choice2 = 2

    first, second = solve()

    res = []
    if first:
        res.append("T")
    else:
        res.append("F")
    if second:
        res.append("T")
    else:
        res.append("F")
    for i in range(2, n):
        if first:
            print(f"-{choice1} {i + 1}", flush=True)
            result = input()
            res.append(result)
        else:
            print(f"{choice1} {i + 1}", flush=True)
            result = input()
            res.append(result)

    print(''.join(res))