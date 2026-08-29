import math

s = int(input())
wumpus_locs = set()

while len(wumpus_locs) < 4:
    s = s + math.floor(s / 13) + 15
    str_s = str(s)
    x = int(str_s[-2])
    y = int(str_s[-1])
    if (x, y) in wumpus_locs:
        continue
    wumpus_locs.add((x, y))

count = 0
while len(wumpus_locs) > 0:
    count += 1
    guess = input()
    x = int(guess[0])
    y = int(guess[1])
    if (x, y) in wumpus_locs:
        print("You hit a wumpus!")
        wumpus_locs.remove((x, y))
    if len(wumpus_locs) == 0:
        print(f"Your score is {count} moves.") 
    else:
        mini = float('inf')
        for wump_x, wump_y in wumpus_locs:
            mini = min(mini, abs(wump_x - x) + abs(wump_y - y))
        print(mini)