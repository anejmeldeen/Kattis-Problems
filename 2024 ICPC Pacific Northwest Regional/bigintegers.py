t = int(input())
for _ in range(t):
    first = input()
    second = input()

    char_to_int = {e: i for i, e in enumerate("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    first_smaller = len(first) < len(second)
    if len(first) == len(second):
        n = len(first)
        for i in range(n):
            if char_to_int[first[i]] < char_to_int[second[i]]:
                first_smaller = True
                break
            elif char_to_int[second[i]] < char_to_int[first[i]]:
                first_smaller = False
                break

    if first_smaller:
        if first < second:
            print("YES")
        else:
            print("NO")
    else:
        if first < second:
            print("NO")
        else:
            print("YES")