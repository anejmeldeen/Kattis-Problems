n = int(input())

even = False
nonzero_even = False
odd = False
nonfive_odd = False

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even = True
        if num != 0:
            nonzero_even = True
    elif num % 2 == 1:
        odd = True
        if num != 5:
            nonfive_odd = True

if (nonzero_even and odd) or (nonfive_odd):
    print(1)
else:
    print(n)