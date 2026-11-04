n = int(input())

doubles = set()
triples = set()

words = []
for _ in range(n):
    word = input()
    if len(word) != len(set(word)) or word in triples:
        continue
    triples.add(word)
    doubles.add(word[:2])
    words.append(list(word))

sol = 0
n = len(words)

count = 0
grid = [None, None, None]
for i in range(n):
    grid[0] = words[i]
    letters = words[i]
    for j in range(n):
        if i == j:
            continue

        grid[1] = words[j]
        new_letters = letters + words[j]
        if len(new_letters) != len(set(new_letters)):
            continue
        if grid[0][0] + grid[1][0] not in doubles:
            continue
        if grid[0][1] + grid[1][1] not in doubles:
            continue
        if grid[0][2] + grid[1][2] not in doubles:
            continue
        if grid[0][0] + grid[1][1] not in doubles:
            continue
        if grid[0][2] + grid[1][1] not in doubles:
            continue

        for k in range(n):
            if i == k or j == k:
                continue

            grid[2] = words[k]
            final_letters = new_letters + words[k]
            
            if len(final_letters) != len(set(final_letters)):
                continue

            group = [''.join(grid[0]), ''.join(grid[1]), ''.join(grid[2])]
            if grid[0][0] + grid[1][0] + grid[2][0] not in triples:
                continue
            if grid[0][1] + grid[1][1] + grid[2][1] not in triples:
                continue
            if grid[0][2] + grid[1][2] + grid[2][2] not in triples:
                continue
            if grid[0][0] + grid[1][1] + grid[2][2] not in triples:
                continue
            if grid[0][2] + grid[1][1] + grid[2][0] not in triples:
                continue

            sol += 1

print(sol)