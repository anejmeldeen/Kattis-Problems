from collections import defaultdict

n = int(input())

words_by_length = defaultdict(list)

for _ in range(n):
    word = input()
    words_by_length[len(word)].append(word)

total = 0
for k in words_by_length:
    words = words_by_length[k]
    found = set()
    bad = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word_i = words[i]
            word_j = words[j]
            first_diff = -1
            for m in range(k):
                if word_i[m] != word_j[m]:
                    first_diff = m
                    break
            if m < k - 1 and word_i[first_diff + 1] != word_j[first_diff + 1] and word_i[first_diff + 2:] == word_j[first_diff + 2:]:
                key = (*sorted([word_i[first_diff:first_diff + 2], word_j[first_diff:first_diff + 2]]), first_diff)
                if key in bad:
                    continue
                if key not in found:
                    found.add(key)
                else:
                    found.remove(key)
                    bad.add(key)
    total += len(found)
print(total)