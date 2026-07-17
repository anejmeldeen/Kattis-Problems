r, g, b = list(map(int, input().split()))
r_have, g_have, b_have = list(map(int, input().split()))
rg, gb = list(map(int, input().split()))

r -= r_have
g -= g_have
b -= b_have

r = max(r, 0)
g = max(g, 0)
b = max(b, 0)

total = r + g + b
possible = True

rg -= r
gb -= b
if rg < 0 or gb < 0:
    possible = False
rem = rg + gb
rem -= g
if rem < 0:
    possible = False

if possible:
    print(total)
else:
    print(-1)