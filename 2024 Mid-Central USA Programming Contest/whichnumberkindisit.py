import math

t = int(input())
for _ in range(t):
    n = int(input())
    odd, square = False, False
    if n % 2 == 1:
        odd = True
    if int(math.sqrt(n)) ** 2 == n:
        square = True

    if odd and square:
        print("OS")
    elif odd:
        print("O")
    elif square:
        print("S")
    else:
        print("EMPTY")