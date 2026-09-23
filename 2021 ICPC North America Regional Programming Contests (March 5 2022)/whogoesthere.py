n, m = list(map(int, input().split()))
schools = []
for _ in range(m):
    schools.append(int(input()))

get = [0] * m
while n > 0:
    for i in range(m):
        if schools[i] > 0:
            schools[i] -= 1
            get[i] += 1
            n -= 1
        if n == 0:
            break

for ele in get:
    print(ele)