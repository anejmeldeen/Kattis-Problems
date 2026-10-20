time1 = list(map(int, input().split(" : ")))
time2 = list(map(int, input().split(" : ")))


midnight = 3600 * 24
time1 = 3600 * time1[0] + 60 * time1[1] + time1[2]
time2 = 3600 * time2[0] + 60 * time2[1] + time2[2]

if time1 < time2:
    print(time2 - time1)
else:
    print(midnight - time1 + time2)