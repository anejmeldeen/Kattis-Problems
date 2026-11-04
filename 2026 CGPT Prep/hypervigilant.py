t = int(input())
for _ in range(t):
    n = int(input())

    rows = set()
    cols = set()
    pos_diags = set()
    neg_diags = set()

    works = True
    for _ in range(n):
        a, b = list(map(int, input().split()))
        if a in rows or b in cols or a + b in neg_diags or a - b in pos_diags:
            works = False
        rows.add(a)
        cols.add(b)
        neg_diags.add(a + b)
        pos_diags.add(a - b)

    print("YES" if works else "NO")