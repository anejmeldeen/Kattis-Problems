n, s = list(map(int, input().split()))
maxi = s
total = 0
for _ in range(n):
    order = input()
    consume = int(order[0])
    if len(order) > 1:
        consume += 1
    if consume > s:
        s = maxi
        total += 1
    s -= consume
print(total)