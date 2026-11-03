r, c1, c2 = list(map(int, input().split()))

first = []
second = []
for _ in range(r):
    first.append(list(map(int, list(input()))))
for _ in range(r):
    second.append(list(map(int, list(input()))))

first_one_row = -1
for j in range(c2):
    for i in range(r):
        if second[i][j] == 1:
            first_one_row = j
    if first_one_row != -1:
        break

c2 -= j
for i in range(r):
    second[i] = second[i][first_one_row:]

works = False
for spot in range(c1 + 1):
    grid = [[(0, 0)] * (c1 + c2) for _ in range(r)]

    for i in range(r):
        for j in range(c1):
            grid[i][j] = (first[i][j], 0)

    this_one = True
    for i in range(r):
        for j in range(c2):
            if second[i][j] == 1:
                if grid[i][j + spot][0] == 1:
                    this_one = False
                grid[i][j + spot] = (second[i][j], 1)

    smallest_x, smallest_y = float('inf'), float('inf')
    largest_x, largest_y = float('-inf'), float('-inf')
    left_most_0 = float('inf')
    right_most_0 = float('-inf')
    left_most_1 = float('inf')
    right_most_1 = float('-inf')

    for i in range(r):
        for j in range(c1 + c2):
            if grid[i][j][0] == 1:
                smallest_x = min(smallest_x, i)
                smallest_y = min(smallest_y, j)
                largest_x = max(largest_x, i)
                largest_y = max(largest_y, j)
                if grid[i][j][1] == 1:
                    left_most_1 = min(left_most_1, j)
                    right_most_1 = max(right_most_1, j)
                else:
                    left_most_0 = min(left_most_0, j)
                    right_most_0 = max(right_most_0, j)

    for i in range(smallest_x, largest_x + 1):
        for j in range(smallest_y, largest_y + 1):
            if grid[i][j][0] == 0:
                this_one = False

    if left_most_0 > left_most_1:
        this_one = False
    if right_most_1 < right_most_0:
        this_one = False

    works = works or this_one

print("Yes" if works else "No")