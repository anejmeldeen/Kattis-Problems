def simplex(c, A, b):
    m, n = len(A), len(c)
    if any(v < 0 for v in b):
        raise ValueError("Requires b >= 0; use two-phase simplex otherwise")
    basis = [n + i for i in range(m)]
    
    # Tableau: [ A | I | b ] over [ -c | 0 | 0 ]
    tab = [row[:] + [1 if i == j else 0 for j in range(m)] + [b[i]] 
           for i, row in enumerate(A)]
    tab.append([-x for x in c] + [0] * (m + 1))
    
    while True:
        c_idx = next(
            (j for j in range(n + m) if tab[-1][j] < -1e-9),
            -1
        )
        if c_idx == -1:
            break
            
        candidates = [
            i for i in range(m) if tab[i][c_idx] > 1e-9
        ]
        if not candidates:
            return float('inf'), []
            
        r_idx = min(
            candidates,
            key=lambda i: (tab[i][-1] / tab[i][c_idx], basis[i])
        )
        
        pivot = tab[r_idx][c_idx]
        for j in range(n + m + 1): tab[r_idx][j] /= pivot
        for i in range(m + 1):
            if i != r_idx:
                fact = tab[i][c_idx]
                for j in range(n + m + 1): 
                    tab[i][j] -= fact * tab[r_idx][j]
                    
        basis[r_idx] = c_idx
        
    ans = [0.0] * n
    for i in range(m):
        if basis[i] < n:
            ans[basis[i]] = tab[i][-1]
            
    return tab[-1][-1], ans

n, m = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [[] for _ in range(n)]

c = []

for _ in range(m):
    items = list(map(float, input().split()))
    c.append(items[-1])
    for i in range(len(items) - 1):
        a[i].append(items[i] / 100)

res = simplex(c, a, b)[0]

print(f"{res:0.2f}")