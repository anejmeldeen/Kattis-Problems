num = input()
int_num = int(num)
num = list(map(int, list(num)))
taken = set(num)

if len(taken) == 10:
    print("Impossible")
    exit()

res = []
first_larger = num[0]
while first_larger in taken:
    first_larger += 1
if first_larger != 10:
    lowest = 0
    while lowest in taken:
        lowest += 1
    res = [first_larger] + [lowest] * (len(num) - 1)

res2 = []
first_smaller = num[0]
while first_smaller in taken:
    first_smaller -= 1
if first_smaller != -1:
    largest = 9
    while largest in taken:
        largest -= 1
    res2 = [first_smaller] + [largest] * (len(num) - 1)

sols = []
best = float('inf')
if res:
    int_res1 = int(''.join(list(map(str, res))))
    if abs(int_num - int_res1) < best:
        best = abs(int_num - int_res1)
        sols = [int_res1]
if res2:
    int_res2 = int(''.join(list(map(str, res2))))
    if abs(int_num - int_res2) < best:
        best = abs(int_num - int_res2)
        sols = [int_res2]
    elif abs(int_num - int_res2) == best:
        sols.append(int_res2)

if len(num) >= 2:
    largest = 9
    while largest in taken:
        largest -= 1
    res3 = [largest] * (len(num) - 1)
    int_res3 = int(''.join(list(map(str, res3))))
    if abs(int_num - int_res3) < best:
        best = abs(int_num - int_res3)
        sols = [int_res3]
    elif abs(int_num - int_res3) == best:
        sols.append(int_res3)

smallest = 1
while smallest in taken:
    smallest += 1
if smallest != 10:
    next_smallest = 0
    while next_smallest in taken:
        next_smallest += 1
    res4 = [smallest] + [next_smallest] * len(num)
    int_res4 = int(''.join(list(map(str, res4))))
    if abs(int_num - int_res4) < best:
        best = abs(int_num - int_res4)
        sols = [int_res4]
    elif abs(int_num - int_res4) == best:
        sols.append(int_res4)

sols = list(set(sols))
sols.sort()
print(' '.join(list(map(str, sols))))