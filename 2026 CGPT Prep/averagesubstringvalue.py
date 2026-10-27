from fractions import Fraction

arr = list(map(int, list(input())))
n = len(arr)
arr.append(float('inf'))

total = 0
stack = [(float('inf'), -1)]
for i, ele in enumerate(arr):
    while stack[-1][0] < ele:
        old_ele, old_idx = stack.pop()
        total += (i - old_idx) * (old_idx - stack[-1][1]) * old_ele
    stack.append((ele, i))

numer = total
denom = n * (n + 1) // 2
inty = numer // denom
frac = Fraction(numer % denom, denom)

if numer % denom == 0:
    print(inty)
elif inty == 0:
    print(f"{frac.numerator}/{frac.denominator}")
else:
    print(f"{inty} {frac.numerator}/{frac.denominator}")