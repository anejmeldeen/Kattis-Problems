n = int(input())
orders = input()

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
        m1 = lcm
    return res

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letters = letters[:n]

rems = []
mods = []

for i in range(n):
    val = orders[i]
    idx = letters.index(val)
    letters.remove(val)

    rems.append(idx)
    mods.append(n - i)

res = gcrt(rems, mods)
if res == -1:
    print("NO")
else:
    print("YES")
    print(res)