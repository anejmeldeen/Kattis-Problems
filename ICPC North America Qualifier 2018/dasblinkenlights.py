p, q, s = list(map(int, input().split()))

yay = False
for i in range(1, s + 1):
    if i % p == 0 and i % q == 0:
        yay = True

print("yes" if yay else "no")