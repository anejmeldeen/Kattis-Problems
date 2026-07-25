w, h, n = list(map(int, input().split()))
have = list(map(int, input().split()))

sol = 0
covered_squares = 0
for k in range(n - 1, -1, -1):
    side_len = (1 << k)
    available = have[k]

    x_squares = w // side_len
    y_squares = h // side_len
    total_squares = x_squares * y_squares

    covered_squares *= 4
    available_squares = total_squares - covered_squares
    available_squares = min(available_squares, available)

    sol += available_squares
    covered_squares += available_squares

if covered_squares == w * h:
    print(sol)
else:
    print(-1)