scores = input().split()

if scores[0][-1] == "6" and scores[1][-1] == "7":
    print(0)
    exit()

scores = [scores[0][-1], scores[1][-1]]
scores = list(map(int, scores))

cost1 = 0
cost2 = 0

def solve(scores):
    res = 0
    if scores[0] > 5:
        res += 15 - scores[0]
    else:
        res += 5 - scores[0]
    if scores[1] > 7:
        res += 17 - scores[1]
    else:
        res += 7 - scores[1]
    return res

print(min(solve(scores), solve(scores[::-1])) + 1)