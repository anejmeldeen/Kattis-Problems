n = int(input())
string = input()

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
chars = alpha[:n]

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

vals = []

for i in range(n):
    length = n - i
    actual = string[i]
    idx = chars.index(actual)
    chars.remove(actual)
    vals.append((length, idx))

rems = [vals[i][1] for i in range(n)]
mods = [vals[i][0] for i in range(n)]
res = gcrt(rems, mods)

if res == -1:
    print("NO")
else:
    print("YES")
    print(res)