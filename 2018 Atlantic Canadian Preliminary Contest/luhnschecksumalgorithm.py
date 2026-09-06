t = int(input())
for _ in range(t):
    num = list(map(int, list(input())))
    count = 0
    for i in range(len(num) - 1, -1, -1):
        count += 1
        if count % 2 == 0:
            num[i] *= 2
            if num[i] >= 10:
                str_num = str(num[i])
                new = int(str_num[0]) + int(str_num[1])
                num[i] = new
    total = sum(num)
    print("PASS" if total % 10 == 0 else "FAIL")