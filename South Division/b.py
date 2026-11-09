import math

n, x, y, z = list(map(int, input().split()))

def grab_dist(x, y):
    x, y = min(x, y), max(x, y)
    return min(abs(x - y), x + n - y)

dists = [grab_dist(x, y), grab_dist(y, z), grab_dist(x, z)]
curr = (max(dists) + min(dists)) / 2

maxi = 0
for x in dists:
    maxi = max(maxi, math.ceil(abs(x - curr)))
print(maxi)