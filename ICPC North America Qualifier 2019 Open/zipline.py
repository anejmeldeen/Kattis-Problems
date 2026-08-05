n = int(input())
AMPLIFIER = 100000

for _ in range(n):
    w, g, h, r = list(map(int, input().split()))
    larger = max(g, h)
    smaller = min(g, h)

    diff = larger - smaller
    hypot = (w ** 2 + diff ** 2) ** 0.5

    longest = float('inf')
    left = 0
    right = w * AMPLIFIER
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3

        w1 = mid1 / AMPLIFIER
        w2 = mid2 / AMPLIFIER

        num1 = (w1 ** 2 + (smaller - r) ** 2) ** 0.5 + ((w - w1) ** 2 + (larger - r) ** 2) ** 0.5
        num2 = (w2 ** 2 + (smaller - r) ** 2) ** 0.5 + ((w - w2) ** 2 + (larger - r) ** 2) ** 0.5
        longest = min(longest, num1, num2)

        if num1 <= num2:
            right = mid2 - 1
        else:
            left = mid1 + 1

    print(hypot, longest)