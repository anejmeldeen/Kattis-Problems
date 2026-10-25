import sys

n = int(input())

left = 1
right = n
while left < right:
    mid1 = (left + right) // 2
    mid2 = mid1 + 1

    print(f"? {mid1}")
    sys.stdout.flush()
    val1 = int(input())

    print(f"? {mid2}")
    sys.stdout.flush()
    val2 = int(input())

    if val2 > val1:
        left = mid2
    else:
        right = mid1

print(f"! {left}")
sys.stdout.flush()