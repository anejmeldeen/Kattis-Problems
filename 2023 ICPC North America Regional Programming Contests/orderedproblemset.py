n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

answers = []
for k in range(2, n + 1):
    if n % k != 0:
        continue
    per_k = n // k
    prev_max = -1
    possible = True
    for i in range(k):
        maxi = -1
        mini = float('inf')
        for j in range(per_k):
            idx = i * per_k + j
            maxi = max(maxi, arr[idx])
            mini = min(mini, arr[idx])

        if mini < prev_max:
            possible = False
            break
            
        prev_max = maxi
    
    if possible:
        answers.append(k)

if len(answers) == 0:
    print(-1)
else:
    for ans in answers:
        print(ans)