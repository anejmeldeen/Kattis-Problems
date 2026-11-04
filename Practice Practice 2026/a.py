d = int(input())

maxi = 0
for i in range(0, 10 * d + 1, 10):
    maxi = max(maxi, i % d)

print(maxi)