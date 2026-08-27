l, h = list(map(int, input().split()))
count = 0
for num in range(l, h + 1):
    works = True
    str_num = str(num)
    for char in str_num:
        dig = int(char)
        if dig == 0 or num % dig != 0:
            works = False
    if len(str_num) != len(set(str_num)):
        works = False
    if works:
        count += 1

print(count)