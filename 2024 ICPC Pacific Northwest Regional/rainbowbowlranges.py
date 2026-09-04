n, m = list(map(int, input().split()))
arr = []

for _ in range(m):
    arr.append(int(input()))

arr.sort()
opp = [n - x for x in arr]

idx = 0
while idx < m:
    if opp[idx] == 0:
        break
    idx += 1

first = opp[0]
opp = opp[1:idx]
opp = opp[::-1]
prefix_sum = [0] * (len(opp) + 1)

for i in range(1, len(opp) + 1):
    prefix_sum[i] = prefix_sum[i - 1] + opp[i - 1]

for k in range(len(opp), -1, -1):
    if k == 0:
        print(1)
        exit()
    summ = first + k + prefix_sum[k] + 1
    if summ <= n:
        print(k + 1)
        exit()