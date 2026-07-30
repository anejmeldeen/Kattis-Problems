n = int(input())
string = input() + "R"

construct = []
low = 1

idx = 0
count = 0
for idx in range(n):
    if string[idx] == "R":
        construct.append(low + count)
        for i in range(low + count - 1, low - 1, -1):
            construct.append(i)
        low = low + count + 1
        count = 0
    else:
        count += 1

for num in construct:
    print(num)