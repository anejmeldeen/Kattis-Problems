n = int(input())
char_to_int = {e: i for i, e in enumerate("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}
for _ in range(n):
    a, b = input().split()
    a_arr, b_arr = [], []
    for char in a:
        a_arr.append(char_to_int[char])
    for char in b:
        b_arr.append(char_to_int[char])
    a, b = a_arr, b_arr

    full_break = False
    for x in range(2, 7501):
        works = True
        a_count = 0
        for val in a:
            if val >= x:
                works = False
                break
            a_count *= x
            a_count += val
        if not works:
            continue

        left = 2
        right = 7500
        while left <= right:
            y = (left + right) // 2
            b_count = 0
            works = True

            for val in b:
                if val >= y:
                    works = False
                    break
                b_count *= y
                b_count += val

            if not works:
                left = y + 1
                continue

            if a_count == b_count:
                print(a_count, x, y)
                full_break = True
                break
            elif a_count > b_count:
                left = y + 1
            else:
                right = y - 1
        if full_break:
            break

    if not full_break:
        print("CANNOT MAKE EQUAL")