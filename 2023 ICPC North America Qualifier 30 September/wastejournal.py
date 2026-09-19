n, a, b = list(map(int, input().split()))
nums = []
impossible = False
for i in range(n - 1):
    nums.append(int(input()))
    if nums[-1] < a or nums[-1] > b:
        impossible = True
nums.sort()

if impossible or b < a:
    print(-1)
elif nums[0] == a and nums[-1] == b:
    for i in range(a, b + 1):
        print(i)
elif nums[0] != a and nums[-1] != b:
    print(-1)
elif nums[0] != a:
    print(a)
else:
    print(b)