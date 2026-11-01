from collections import defaultdict

n = int(input())

words = []
for _ in range(n):
    idx_map = {}
    idx = 0

    word = input()
    arr = []
    for char in word:
        if char not in idx_map:
            idx_map[char] = idx
            idx += 1
        arr.append(idx_map[char])

    idx_map = {}
    idx = 0
    other_arr = []
    for char in word[::-1]:
        if char not in idx_map:
            idx_map[char] = idx
            idx += 1
        other_arr.append(idx_map[char])
    words.append((''.join(list(map(str, arr))), ''.join(list(map(str, other_arr)))))

counts = defaultdict(int)
total = 0
for word in words:
    total += counts[word[0]]
    counts[word[0]] += 1

    if word[0] != word[1]:
        total += counts[word[1]]

print(total)