n = int(input())
arr = []

while len(arr) < n:
    arr += list(map(int, input().split()))
arr += [-1]

stack = []
best = -1
s = 0
e = 0

for i in range(n + 1):
    taken_off = 0
    while stack and stack[-1][0] >= arr[i]:
        last = stack.pop()
        curr = (i - last[1]) * last[0]

        if curr > best:
            best = curr
            s = last[1] + 1
            e = i
        if curr == best and last[1] + 1 <= s:
            s = last[1] + 1
            e = i

        taken_off = max(taken_off, i - last[1])
    
    stack.append((arr[i], i - taken_off))

print(s, e, best)