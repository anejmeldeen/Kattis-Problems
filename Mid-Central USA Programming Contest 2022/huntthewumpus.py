import math

s = int(input())
locations = []

while len(locations) < 4:
    new_s = s + math.floor(s / 13) + 15
    x = (new_s % 100) // 10
    y = new_s % 10

    s = new_s

    if (x, y) in locations:
        continue

    locations.append((x, y))

moves = 0
while True:
    guess = input()
    x = int(guess[0])
    y = int(guess[1])
    moves += 1

    if (x, y) in locations:
        locations.remove((x, y))
        print("You hit a wumpus!")

    if len(locations) == 0:
        break

    min_dist = float('inf')
    for loc_x, loc_y in locations:
        min_dist = min(min_dist, abs(loc_x - x) + abs(loc_y - y))
    
    print(min_dist)

print(f"Your score is {moves} moves.")