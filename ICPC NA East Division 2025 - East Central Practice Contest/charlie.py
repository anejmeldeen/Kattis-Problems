from collections import deque

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr = [(x, i) for i, x in enumerate(arr)]
arr.sort(reverse=True)

queue = deque()

possible = True
res = [0] * n
poss = deque()

for num, index in arr:
    while queue and queue[0][0] >= num:
        data = queue.popleft()
        poss.append([2, data[1]])

    if len(poss) == 0:
        if (num, index) != arr[0]:
            possible = False
            break
    else:
        poss[0][0] -= 1
        res[index] = poss[0][1] + 1
        if poss[0][0] == 0:
            poss.popleft()
    
    queue.append((num - k, index))


if possible:
    print(' '.join(list(map(str, res))))
else:
    print(-1)