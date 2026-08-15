import math

test_case = 1
while (data := input()) != "0 0":
    w, n = list(map(int, data.split()))
    words = []
    c_max = float('-inf')
    for _ in range(n):
        word, size = input().split()
        words.append((word, int(size)))
        c_max = max(c_max, int(size))

    total_height = 0
    curr_height = 0
    curr_width = 0
    for word in words:
        size = 8 + math.ceil((40 * (word[1] - 4)) / (c_max - 4))
        width = math.ceil(9 / 16 * size * len(word[0]))
        if curr_width + width + 10 > w:
            total_height += curr_height
            curr_height = size
            curr_width = width
        else:
            if curr_width != 0:
                curr_width += 10
            curr_width += width
            curr_height = max(curr_height, size)

    print(f"CLOUD {test_case}: {total_height + curr_height}")
    test_case += 1