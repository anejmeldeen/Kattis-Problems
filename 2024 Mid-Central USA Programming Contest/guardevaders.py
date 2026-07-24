from functools import cache

g, p = list(map(int, input().split()))
facing = input()

@cache
def recurse(guards):
    openings = []
    for i in range(g - 1):
        if guards[i] != "R" and guards[i + 1] != "L":
            openings.append(i)

    best = 0
    for opening in openings:
        new_str = ""
        idx = 0
        while idx < g:
            if idx == opening:
                new_str += "RL"
                idx += 2
            else:
                new_str += guards[idx]
                idx += 1
        best = max(best, recurse(new_str))

    return best + (len(openings) > 0)

sol = recurse(facing)
if sol >= p:
    print(1)
else:
    print(0)