n = int(input())
inputs = []
for _ in range(n):
    t, i = list(map(int, input().split()))
    inputs.append((i, t))
inputs.sort()

lag = 0
time = 1
for i in range(n):
    lag += max(0, inputs[i][1] - time)
    time = max(time, inputs[i][1])
    time += 1

print(lag)