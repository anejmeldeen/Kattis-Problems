P = int(input())
for _ in range(P):
    k, frac = input().split()
    k = int(k)

    nums = list(map(int, frac.split("/")))
    num = nums[0]
    den = nums[1]

    if den == 1:
        den = num + 1
        num = 1
    else:
        actions = max((num - den) // den + 1, 0)
        num -= den * actions

        den -= num
        num += den

        den += num * actions
            

    print(k, f"{num}/{den}")