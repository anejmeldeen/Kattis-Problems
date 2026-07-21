seed = int(input())
board = [[0] * 10 for _ in range(10)]

def modify_seed():
    global seed
    seed = seed + (seed // 13) + 15

count = 0
while count < 4:
    modify_seed()
    x = (seed % 100) // 10
    y = seed % 10
    if board[x][y] == 0:
        board[x][y] = 1
        count += 1

hit = 0
score = 0
while True:
    score += 1
    guess = input()
    x = int(guess[0])
    y = int(guess[1])

    if board[x][y] == 1:
        print("You hit a wumpus!")
        board[x][y] = 0
        hit += 1
    
    if hit == 4:
        print(f"Your score is {score} moves.")
        break

    closest = float('inf')
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                closest = min(closest, abs(i - x) + abs(j - y))
    print(closest)