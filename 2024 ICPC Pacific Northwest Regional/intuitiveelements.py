t = int(input())
for _ in range(t):
    element = input()
    abbreviation = input()
    seen = set(element)
    have = set(abbreviation)

    works = True
    for char in have:
        if char not in seen:
            works = False

    print("YES" if works else "NO")