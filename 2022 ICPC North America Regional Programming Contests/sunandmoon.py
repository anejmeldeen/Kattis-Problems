a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

first = (-a) % b
second = (-c) % d

def ext_gcd(a, b):
    if b == 0: return 1, 0, a
    x, y, g = ext_gcd(b, a % b)
    return y, x - y * (a // b), g

def gcrt(rems, mods):
    res, m1 = rems[0], mods[0]
    for r2, m2 in zip(rems[1:], mods[1:]):
        x, y, g = ext_gcd(m1, m2)
        if (r2 - res) % g != 0: return -1
        lcm = (m1 // g) * m2
        res = (res + x * ((r2 - res) // g) % (m2 // g) * m1) % lcm
    return res

rems = [first, second]
mods = [b, d]

print(gcrt(rems, mods))