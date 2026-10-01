import math

r, c = list(map(int, input().split()))

if c == 1:
    print(1)
elif r == 1:
    print(math.ceil(c / 3))
elif r == 2:
    print(math.ceil((c + 1) / 2))
else:
    print(-1)