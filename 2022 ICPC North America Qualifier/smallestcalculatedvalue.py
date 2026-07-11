a, b, c = list(map(int, input().split()))

def recurse(a, b, c, used_b):
    options = []
    if not used_b:
        options.append(recurse(a + b, b, c, True))
        options.append(recurse(a * b, b, c, True))
        options.append(recurse(a - b, b, c, True))
        if a % b == 0:
            options.append(recurse(a // b, b, c, True))
    else:
        options.append(a + c)
        options.append(a - c)
        options.append(a * c)
        if a % c == 0:
            options.append(a // c)

    mini = float('inf')
    for op in options:
        if op >= 0:
            mini = min(mini, op)
    
    return mini

print(recurse(a, b, c, False))