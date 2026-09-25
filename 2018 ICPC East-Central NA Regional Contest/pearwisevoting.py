n, m = list(map(int, input().split()))

ballots = []
for _ in range(m):
    data = input().split()
    ballots.append((int(data[0]), data[1]))

beats = {}
for i in range(n):
    beats[chr(ord('A') + i)] = []

for i in range(n):
    for j in range(i + 1, n):
        char_i = chr(ord('A') + i)
        char_j = chr(ord('A') + j)
        i_count = 0
        j_count = 0
        for ballot in ballots:
            for char in ballot[1]:
                if char == char_i:
                    i_count += ballot[0]
                    break
                elif char == char_j:
                    j_count += ballot[0]
                    break
        if i_count > j_count:
            beats[char_i].append(char_j)
        else:
            beats[char_j].append(char_i)

for i in range(n):
    char = chr(ord('A') + i)
    seen = set()

    def dfs(char):
        if char in seen:
            return
        seen.add(char)

        for b in beats[char]:
            dfs(b)

    dfs(char)
    if len(seen) == n:
        print(f"{char}: can win")
    else:
        print(f"{char}: can't win")