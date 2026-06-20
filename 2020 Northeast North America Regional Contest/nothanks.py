n = int(input())
arr = list(map(int, input().split()))
arr.sort()

prev = float('-inf')
total = 0
for ele in arr:
    if ele != prev + 1:
        total += ele
    prev = ele

print(total)