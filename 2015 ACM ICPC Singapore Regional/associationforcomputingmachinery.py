n, p = list(map(int, input().split()))
arr = list(map(int, input().split()))

time = 0
starter = arr[p]

arr = arr[:p] + arr[p + 1:]
arr.sort()
arr = [starter] + arr

count = 0
penalty = 0

for i in range(n):
    time += arr[i]
    if time <= 300:
        count += 1
        penalty += time
    else:
        break

print(count, penalty)