n, k = list(map(int, input().split()))
ratings = []
for _ in range(2 ** n):
    ratings.append(int(input()))

def recurse(ratings):
    if len(ratings) == 0:
        return 0
    ratings.sort(reverse=True)
    length = len(ratings)
    top_half = ratings[:length // 2]
    bottom_half = ratings[length // 2:]

    idx = 0
    count = 0
    for ele in bottom_half:
        while idx < len(top_half) and top_half[idx] - ele > k:
            idx += 1
        if idx < len(top_half):
            count += 1
            idx += 1

    return count + recurse(top_half)

print(recurse(ratings))