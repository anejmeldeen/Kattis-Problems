from itertools import permutations

n = int(input())
words = []

for _ in range(n):
    words.append(input())

def merge(first, second):
    end, start = "", ""
    poss = []
    for i in range(min(len(first), len(second))):
        end = first[-(i + 1):]
        start = second[:i + 1]
        if end == start:
            poss.append(first[:-(i + 1)] + second)
    return poss


def solve(arr, count):
    if count == 1:
        return arr[0]
    ultimatum = None
    for i in range(count):
        for j in range(count):
            if i == j:
                continue
            first = arr[i]
            second = arr[j]
            poss = merge(first, second)

            new = []
            for k in range(count):
                if k == i or k == j:
                    continue
                new.append(arr[k])
            best = None
            for p in poss:
                final = new.copy()
                final.append(p)
                res = solve(final, count - 1)
                if best == None:
                    best = res
                elif not res:
                    pass
                elif len(res) < len(best):
                    best = res
                elif len(res) == len(best) and res < best:
                    best = res
            if ultimatum == None:
                ultimatum = best
            elif not best:
                continue
            elif len(best) < len(ultimatum):
                ultimatum = best
            elif len(best) == len(ultimatum) and best < ultimatum:
                ultimatum = best
    return ultimatum

solution = solve(words, n)
print(solution if solution else -1)