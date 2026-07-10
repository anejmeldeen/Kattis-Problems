original = input()
end = input()

n = len(original)

dis = -1
for i in range(n):
    if original[i] != end[i]:
        dis = i
        top = original[i]
        bot = end[i]
        break

idx = -1
for i in range(n - 1, -1, -1):
    if original[i] == bot and end[i] == top:
        idx = i
        break
    if original[i] != end[i]:
        break

if idx == dis:
    idx = -1

if original[dis:idx + 1][::-1] != end[dis:idx + 1]:
    idx = -1

if idx != -1:
    count = 1
else:
    count = 0

idx1 = dis - 1
idx2 = idx + 1

while idx1 >= 0 and idx2 < n:
    if original[idx1] == original[idx2] and original[idx1] == end[idx1] and original[idx1] == end[idx2]:
        count += 1
    else:
        break
    idx1 -= 1
    idx2 += 1

print(count)