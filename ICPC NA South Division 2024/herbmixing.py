g, r = list(map(int, input().split()))

count = 0
count += 10 * min(r, g)
r, g = (r - min(r, g)), (g - min(r, g))

count += 10 * (g // 3)
g %= 3

count += 3 * (g // 2)
g %= 2

count += g

print(count)