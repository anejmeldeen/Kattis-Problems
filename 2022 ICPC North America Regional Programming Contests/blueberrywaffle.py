f, r = list(map(int, input().split()))
degrees = (r / f) * 180
degrees %= 360
if degrees < 90 or degrees > 270:
    print("up")
else:
    print("down")