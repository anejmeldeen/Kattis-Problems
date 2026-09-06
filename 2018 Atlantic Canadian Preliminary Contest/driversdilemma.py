c, x, m = list(map(float, input().split()))

data = []
for _ in range(6):
    speed, mpg = list(map(float, input().split()))
    data.append((speed, mpg))

data.sort()
data.reverse()
gas = c / 2

for speed, mpg in data:
    used_driving = 1 / mpg * m
    time_spent_driving = 1 / speed * m
    used_leaking = x * time_spent_driving
    if gas >= used_driving + used_leaking:
        print(f"YES {int(speed)}")
        exit()

print("NO")