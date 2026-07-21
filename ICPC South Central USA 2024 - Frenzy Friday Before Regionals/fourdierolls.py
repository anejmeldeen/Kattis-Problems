n = int(input())
nums = list(map(int, input().split()))

count = 4 - n
prod = 1
for _ in range(count):
    prod *= 6
over = prod

if len(nums) != len(set(nums)):
    print(0, over)
else:
    rem = 4 - n
    prod = 1
    count = 6 - n
    for _ in range(rem):
        prod *= count
        count -= 1

    print(prod, over - prod)