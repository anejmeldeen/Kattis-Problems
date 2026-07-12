r, c = list(map(int, input().split()))
MOD = 998244353

poss = r
for _ in range(c - 1):
    poss *= (r - 1)
    poss %= MOD

print(poss)