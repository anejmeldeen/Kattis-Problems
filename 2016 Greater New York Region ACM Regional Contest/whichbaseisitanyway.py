n = int(input())
for _ in range(n):
    k, num = list(map(int, input().split()))

    cpy = num
    octa = 0
    mult = 1
    while num > 0:
        if num % 10 >= 8:
            octa = 0
            break
        octa += (num % 10) * mult
        mult *= 8
        num //= 10

    num = cpy
    hexa = 0
    mult = 1
    while num > 0:
        hexa += (num % 10) * mult
        mult *= 16
        num //= 10

    print(k, octa, cpy, hexa)