s, v1, v2 = list(map(int, input().split()))

for k in range(s // v1, -1, -1):
    rem = s - k * v1
    if rem % v2 == 0:
        print(k, rem // v2)
        exit()

print("Impossible")