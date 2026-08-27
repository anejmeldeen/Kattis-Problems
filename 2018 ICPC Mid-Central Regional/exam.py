k = int(input())
same = diff = 0
a = input()
b = input()

for i in range(len(a)):
    if a[i] == b[i]:
        same += 1
    else:
        diff += 1

total = min(same, k)
l = len(a) - k
total += min(diff, l)

print(total)