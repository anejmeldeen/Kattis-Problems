n, q = list(map(int, input().split()))
mappy = {}
for val in range(n):
    mappy[input()] = val

for _ in range(q):
    first, second = input().split()
    print(abs(mappy[second] - mappy[first]) - 1)