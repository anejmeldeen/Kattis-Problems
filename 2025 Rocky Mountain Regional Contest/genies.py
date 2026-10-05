from functools import cache

w, k, c = list(map(int, input().split()))

dp = [False] * (w + 1)

@cache
def recurse(rank, made_wishes):
    if made_wishes > w:
        return
    if rank < 1:
        dp[made_wishes] = True
        return
    for remove in range(c, rank):
        recurse(rank - remove, made_wishes + rank - 1)
    recurse(0, made_wishes + rank)

recurse(k, 0)

print("yes" if dp[w] else "no")