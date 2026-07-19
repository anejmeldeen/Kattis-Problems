import math

r, c = list(map(int, input().split()))
switch = 0
for i in range(r):
    r = c
    word = input()
    diff = r - len(word)
    if diff % 2 == 0:
        print("." * (diff // 2) + word + "." * (diff // 2))
    else:
        switch += 1
        if switch % 2 == 1:
            diff = r - len(word)
            l = diff // 2
            right = math.ceil(diff / 2)
            print("." * l + word + "." * right)
        else:
            diff = r - len(word)
            l = math.ceil(diff / 2)
            right = diff // 2
            print("." * l + word + "." * right)