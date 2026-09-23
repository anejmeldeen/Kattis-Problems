n = int(input())
menu = list(map(int, input().split()))

MAXI = 30001
dp = [0] * MAXI
dp[0] = 1

m = int(input())
orders = list(map(int, input().split()))
gather = {}

for idx, item in enumerate(menu):
    for i in range(MAXI):
        if dp[i] > 0 and i + item < MAXI:
            dp[i + item] += dp[i]
            gather[i + item] = idx + 1

for order in orders:
    if dp[order] == 0:
        print("Impossible")
    elif dp[order] > 1:
        print("Ambiguous")
    else:
        path = []
        while order in gather:
            path.append(gather[order])
            order -= menu[gather[order] - 1]
        print(' '.join(list(map(str, path[::-1]))))