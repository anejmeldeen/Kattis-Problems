import math

while (n := int(input())) != 0:
    houses = []
    for _ in range(n):
        x, y = list(map(float, input().split()))
        houses.append((x, y))

    def check(check_me):
        max_dist = 0
        for x, y in houses:
            max_dist = max(max_dist, math.sqrt((x - check_me) ** 2 + y ** 2))
        return max_dist

    left = -200000
    right = 200000
    for i in range(100):
        mid1 = left + (right - left) / 3
        mid2 = left + (right - left) * 2 / 3

        try1 = check(mid1)
        try2 = check(mid2)

        if try1 < try2:
            right = mid2
        else:
            left = mid1

    print(round(left, 6), round(check(left), 6))
    input()