n = int(input())
days = set()

for _ in range(n):
    start, end = list(map(int, input().split()))
    for day in range(start, end + 1):
        days.add(day)

print(len(days))