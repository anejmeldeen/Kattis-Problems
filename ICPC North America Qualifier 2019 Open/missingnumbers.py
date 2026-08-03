n = int(input())
seen = set()
for i in range(n):
    num = int(input())
    seen.add(num)
    if i == n - 1:
        last = num

not_in = []
for i in range(1, last + 1):
    if i not in seen:
        not_in.append(i)

if len(not_in) == 0:
    print("good job")
else:
    for ele in not_in:
        print(ele)