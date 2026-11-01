import sys

n = int(input())

sol = []

def recurse(left, right, rem):
    if rem == 0:
        return
    if left == right:
        sol.append(left)
        return
    
    mid = (left + right) // 2
    print(f"? {left} {mid}")
    sys.stdout.flush()

    first_half = int(input())
    recurse(left, mid, first_half)
    recurse(mid + 1, right, rem - first_half)

recurse(1, n, 2)

sol.sort()
print(f"! {sol[0]} {sol[1]}")