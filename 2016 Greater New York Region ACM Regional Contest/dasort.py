import math

p = int(input())
for _ in range(p):
    k, n = list(map(int, input().split()))
    arr = []
    for _ in range(math.ceil(n / 10)):
        arr += list(map(int, input().split()))

    monoton = []

    mini = float('inf')

    for ele in arr:
        while monoton and ele < monoton[-1]:
            mini = min(mini, monoton.pop())
        if ele <= mini:
            monoton.append(ele)
    
    print(k, n - len(monoton))