from collections import defaultdict

n, code, guess = input().split()
n = int(n)

new_code = []
new_guess = []
s = 0
r = 0

for i in range(n):
    if code[i] != guess[i]:
        new_code.append(code[i])
        new_guess.append(guess[i])
    else:
        r += 1

code_counts = defaultdict(int)
guess_counts = defaultdict(int)

for char in new_code:
    code_counts[char] += 1
for char in new_guess:
    guess_counts[char] += 1

for key in code_counts:
    s += min(code_counts[key], guess_counts[key])

print(r, s)