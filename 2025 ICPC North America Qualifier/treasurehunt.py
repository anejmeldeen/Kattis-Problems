def solve(x, y):
    print(f"? {x - 1} {y}")
    res = int(input())
    if res == 1:
        print(f"? {x - 1} {y - 1}")
        res = int(input())
        if res == 1:
            print(f"! {x - 1} {y - 1}")
        else:
            print(f"! {x - 1} {y}")
    else:
        print(f"? {x} {y - 1}")
        res = int(input())
        if res == 1:
            print(f"! {x} {y - 1}")
        else:
            print(f"! {x} {y}")

print("? 4 4")
res = int(input())
if res == 1:
    solve(4, 4)
else:
    print("? 2 2")
    res = int(input())
    if res == 1:
        solve(2, 2)
    else:
        print("? 4 2")
        res = int(input())
        if res == 1:
            solve(4, 2)
        else:
            solve(2, 4)