while True:
    num, denom = list(map(int, input().split()))
    if num == 0 and denom == 0:
        break

    inty = num // denom
    num %= denom

    print(f"{inty} {num} / {denom}")