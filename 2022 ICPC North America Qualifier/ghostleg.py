n, m = list(map(int, input().split()))
sol = [0] * n

rungs = {}
for i in range(1, n + 1):
    rungs[i] = []

for idx in range(m):
    a = int(input())

    rungs[a].append((a + 1, idx))
    rungs[a + 1].append((a, idx))

def recurse(curr_num, curr_index):
    new_rungs = rungs[curr_num]
    next_rung = -1
    for rung in new_rungs:
        if rung[1] > curr_index:
            next_rung = rung
            break
    
    if next_rung == -1:
        return curr_num
    
    else:
        return recurse(next_rung[0], next_rung[1])
    
for num in range(1, n + 1):
    sol[recurse(num, -1) - 1] = num

for ele in sol:
    print(ele)