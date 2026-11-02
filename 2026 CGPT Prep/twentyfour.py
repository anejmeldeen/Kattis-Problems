a, b, c, d = list(map(int, input().split()))

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    if y == 0 or x % y != 0:
        return False
    return x // y

idx_to_func = {0: add, 1: sub, 2: mult, 3: div}

def solve(perm, i, j, k, paren_type):
    a, b, c, d = perm
    i_func = idx_to_func[i]
    j_func = idx_to_func[j]
    k_func = idx_to_func[k]

    if paren_type == 0:
        if i not in [2, 3] and j not in [2, 3]:
            res1 = k_func(c, d)
            if not res1:
                return 0
            res2 = i_func(a, b)
            if not res2:
                return 0
            res3 = j_func(res2, res1)
            return res3 if res3 else 0
        elif i not in [2, 3]:
            res1 = j_func(b, c)
            if not res1:
                return 0
            res2 = k_func(res1, d)
            if not res2:
                return 0
            res3 = i_func(a, res2)
            return res3 if res3 else 0
        else:
            res1 = i_func(a, b)
            if not res1:
                return 0
            if j not in [2, 3]:
                res2 = k_func(c, d)
                if not res2:
                    return 0
                res3 = j_func(res1, res2)
                return res3 if res3 else 0
            else:
                res2 = j_func(res1, c)
                if not res2:
                    return 0
                res3 = k_func(res2, d)
                return res3 if res3 else 0
    elif paren_type == 1:
        res1 = i_func(a, b)
        if not res1:
            return 0
        if j not in [2, 3]:
            res2 = k_func(c, d)
            if not res2:
                return 0
            res3 = j_func(res1, res2)
            return res3 if res3 else 0
        else:
            res2 = j_func(res1, c)
            if not res2:
                return 0
            res3 = k_func(res2, d)
            return res3 if res3 else 0
    elif paren_type == 2:
        res1 = j_func(b, c)
        if not res1:
            return 0
        if i not in [2, 3]:
            res2 = k_func(res1, d)
            if not res2:
                return 0
            res3 = i_func(a, res2)
            return res3 if res3 else 0
        else:
            res2 = i_func(a, res1)
            if not res2:
                return 0
            res3 = k_func(res2, d)
            return res3 if res3 else 0
    elif paren_type == 3:
        res1 = k_func(c, d)
        if not res1:
            return 0
        if i not in [2, 3]:
            res2 = j_func(b, res1)
            if not res2:
                return 0
            res3 = i_func(a, res2)
            return res3 if res3 else 0
        else:
            res2 = i_func(a, b)
            if not res2:
                return 0
            res3 = j_func(res2, res1)
            return res3 if res3 else 0
    elif paren_type == 4:
        if j not in [2, 3]:
            res1 = k_func(c, d)
            if not res1:
                return 0
            res2 = j_func(b, res1)
            if not res2:
                return 0
        else:
            res1 = j_func(b, c)
            if not res1:
                return 0
            res2 = k_func(res1, d)
            if not res2:
                return 0
        res3 = i_func(a, res2)
        return res3 if res3 else 0
    elif paren_type == 5:
        if i not in [2, 3]:
            res1 = j_func(b, c)
            if not res1:
                return 0
            res2 = i_func(a, res1)
            if not res2:
                return 0
        else:
            res1 = i_func(a, b)
            if not res1:
                return 0
            res2 = j_func(res1, c)
            if not res2:
                return 0
        res3 = k_func(res2, d)
        return res3 if res3 else 0
    elif paren_type == 6:
        res1 = i_func(a, b)
        res2 = k_func(c, d)
        if not res1 or not res2:
            return 0
        res3 = j_func(res1, res2)
        return res3 if res3 else 0

permutations = []
permutations.append(([a, b, c, d], 0))
permutations.append(([a, b, d, c], 1))
permutations.append(([a, c, b, d], 1))
permutations.append(([a, c, d, b], 2))
permutations.append(([a, d, c, b], 3))
permutations.append(([a, d, b, c], 2))
permutations.append(([b, a, c, d], 1))
permutations.append(([b, a, d, c], 2))
permutations.append(([b, c, a, d], 2))
permutations.append(([b, c, d, a], 3))
permutations.append(([b, d, a, c], 3))
permutations.append(([b, d, c, a], 4))
permutations.append(([c, b, a, d], 3))
permutations.append(([c, b, d, a], 4))
permutations.append(([c, a, b, d], 2))
permutations.append(([c, a, d, b], 3))
permutations.append(([c, d, a, b], 4))
permutations.append(([c, d, b, a], 5))
permutations.append(([d, a, b, c], 3))
permutations.append(([d, a, c, b], 4))
permutations.append(([d, b, a, c], 4))
permutations.append(([d, b, c, a], 5))
permutations.append(([d, c, a, b], 5))
permutations.append(([d, c, b, a], 6))

best = float('inf')
for perm, cost in permutations:
    cost *= 2
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                res1 = solve(perm, i, j, k, 0)
                res2 = solve(perm, i, j, k, 1)
                res3 = solve(perm, i, j, k, 2)
                res4 = solve(perm, i, j, k, 3)
                res5 = solve(perm, i, j, k, 4)
                res6 = solve(perm, i, j, k, 5)
                res7 = solve(perm, i, j, k, 6)

                if res1 == 24:
                    best = min(best, cost)
                if res2 == 24:
                    best = min(best, cost + 1)
                if res3 == 24:
                    best = min(best, cost + 1)
                if res4 == 24:
                    best = min(best, cost + 1)
                if res5 == 24:
                    best = min(best, cost + 1)
                if res6 == 24:
                    best = min(best, cost + 1)
                if res7 == 24:
                    best = min(best, cost + 2)

if best == float('inf'):
    print("impossible")
else:
    print(best)