n = int(input())
choices = []
for _ in range(n):
    choices.append(int(input()))

sol = min(choices) - max(choices) // 2
if sol < 0:
    print(0)
else:
    print(sol)