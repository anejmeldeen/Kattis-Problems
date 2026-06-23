word = list(input())
a_count = word.count("A")

sol = []

for k in range(1, a_count + 1):
    idx = 0
    a_score = 0
    b_score = 0
    a_count = 0
    b_count = 0
    while idx < len(word):
        if word[idx] == "A":
            a_count += 1
        else:
            b_count += 1

        if a_count == k:
            a_score += 1
            a_count = 0
            b_count = 0
        elif b_count == k:
            b_score += 1
            a_count = 0
            b_count = 0
    
        idx += 1
    
    if a_score > b_score:
        sol.append(k)

print(len(sol))
print(' '.join(list(map(str, sol))))