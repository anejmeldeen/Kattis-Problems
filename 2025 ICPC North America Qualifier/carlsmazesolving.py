r, c = list(map(int, input().split()))
curr_x, curr_y = list(map(int, input().split()))
end_x, end_y = list(map(int, input().split()))

curr_x -= 1
curr_y -= 1
end_x -= 1
end_y -= 1

board = []
for _ in range(r):
    board.append(input())

seen = set()
direction = 0
found = 0
while True:
    if curr_x == end_x and curr_y == end_y:
        found = 1
        break
    if (curr_x, curr_y, direction) in seen:
        break
    seen.add((curr_x, curr_y, direction))

    # turn left and move
    next_x, next_y = -1, -1
    new_dir = -1
    if direction == 0:
        next_x, next_y = curr_x - 1, curr_y
        new_dir = 3
    elif direction == 1:
        next_x, next_y = curr_x, curr_y + 1
        new_dir = 0
    elif direction == 2:
        next_x, next_y = curr_x + 1, curr_y
        new_dir = 1
    elif direction == 3:
        next_x, next_y = curr_x, curr_y - 1
        new_dir = 2

    if next_x >= 0 and next_y >= 0 and next_x < r and next_y < c and board[next_x][next_y] == "0":
        curr_x = next_x
        curr_y = next_y
        direction = new_dir
        continue

    # move forward
    next_x, next_y = curr_x, curr_y
    if direction == 0:
        next_y += 1
    elif direction == 1:
        next_x += 1
    elif direction == 2:
        next_y -= 1
    elif direction == 3:
        next_x -= 1

    if next_x >= 0 and next_y >= 0 and next_x < r and next_y < c and board[next_x][next_y] == "0":
        curr_x = next_x
        curr_y = next_y
        continue

    # turn right
    new_dir = (direction + 1) % 4
    direction = new_dir

print(found)