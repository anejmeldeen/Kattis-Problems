from collections import deque
from fractions import Fraction

number = list(map(int, list(input())))

total = 0

for num in range(10):
    seen = set()
    queue = deque()
    for i, digit in enumerate(number):
        if digit == num:
            queue.append(i)
            seen.add(i)
    while queue:
        location = queue.popleft()
        if location - 1 >= 0 and number[location - 1] < num and (location - 1) not in seen:
            queue.append(location - 1)
            seen.add(location - 1)
        if location + 1 < len(number) and number[location + 1] < num and (location + 1) not in seen:
            queue.append(location + 1)
            seen.add(location + 1)

    intervals = []
    for idx in range(len(number)):
        if idx in seen:
            if intervals and intervals[-1][1] == idx - 1:
                intervals[-1][1] = idx
            else:
                intervals.append([idx, idx])

    adder = 0
    for interval in intervals:
        n = (interval[1] - interval[0] + 1)
        adder += n * (n + 1) // 2

    removal = set()
    for i in range(len(number)):
        if i in seen and number[i] != num:
            removal.add(i)

    intervals = []
    for idx in range(len(number)):
        if idx in removal:
            if intervals and intervals[-1][1] == idx - 1:
                intervals[-1][1] = idx
            else:
                intervals.append([idx, idx])

    old = adder
    for interval in intervals:
        n = (interval[1] - interval[0] + 1)
        adder -= n * (n + 1) // 2
    
    total += adder * num

denom = len(number) * (len(number) + 1) // 2
inty = total // denom
diff = total % denom
frac = Fraction(diff, denom)

if diff == 0:
    print(inty)
elif inty == 0:
    print(f"{frac.numerator}/{frac.denominator}")
else:
    print(f"{inty} {frac.numerator}/{frac.denominator}")