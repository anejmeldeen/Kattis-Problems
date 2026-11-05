import math

distance, speed, hours = list(map(int, input().split()))

circum = 2 * math.pi * distance
time = circum / speed
days = time / hours

print(days)