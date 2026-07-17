arr = list(map(int, input().split()))
last = arr[-1]
digit = last % 10
if digit == 0:
    digit = 10

print(digit)