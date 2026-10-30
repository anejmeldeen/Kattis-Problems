import sys

n = int(input())

# figure out the row
left = 1
right = n
while left < right:
    mid = (left + right) // 2

    print(f"? {left} {mid} {1} {n}")
    sys.stdout.flush()

    val = int(input())
    if val == mid - left + 1:
        left = mid + 1
    else:
        right = mid
row = left

# figure out the col
left = 1
right = n
while left < right:
    mid = (left + right) // 2

    print(f"? {1} {n} {left} {mid}")
    sys.stdout.flush()

    val = int(input())
    if val == mid - left + 1:
        left = mid + 1
    else:
        right = mid
col = left

print(f"! {row} {col}")