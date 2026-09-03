a = input()
b = input()

a = "0" * (len(b) - len(a)) + a

count = 0
for idx in range(len(a)):
    if a[idx] == "1":
        count += 1
    if a[idx] == "0" and b[idx] == "1":
        count += len(b) - idx
        break
print(count)