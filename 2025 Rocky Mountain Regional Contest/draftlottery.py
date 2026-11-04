n = int(input())

total_balls = 0
count = {}

for _ in range(n):
    balls, team_name = input().split()
    count[team_name] = int(balls)
    total_balls += int(balls)

q = int(input())
for _ in range(q):
    team, placement = list(map(int, input().split()))
    