r, f = list(map(int, input().split()))

rotations = f // r
leftover = f % r
if leftover > (r // 2):
    rotations += 1

if rotations % 2 == 0:
    print("up")
else:
    print("down")