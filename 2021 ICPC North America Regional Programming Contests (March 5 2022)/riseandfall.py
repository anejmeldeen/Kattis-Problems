t = int(input())
for _ in range(t):
    n = list(input())
    decreasing = False
    decre = False
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            if decre:
                n[i] = n[i - 1]
            decreasing = True
        elif n[i] > n[i - 1]:
            if decreasing:
                n[i] = n[i - 1]
                decre = True
    print(''.join(n))