import math

c = int(input())
arr = list(map(int, input().split()))
arr.sort()

need = math.ceil((sum(arr) + 1) / 2)
cand = arr[-2]

rounds = 0
for i in range(c - 2):
    rounds += 1
    cand += arr[i]
    if cand >= need:
        break

if cand >= need:
    print(rounds)
else:
    print("IMPOSSIBLE TO WIN")