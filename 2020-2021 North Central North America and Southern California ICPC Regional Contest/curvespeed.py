import sys, math

data = sys.stdin.readlines()
for item in data:
    r, s = list(map(float, item.split()))
    print(round(math.sqrt(r * (s + .16) / .067)))