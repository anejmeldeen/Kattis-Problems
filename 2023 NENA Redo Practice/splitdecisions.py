from collections import defaultdict

length_to_words = defaultdict(list)

n = int(input())

for _ in range(n):
    word = input()
    length_to_words[len(word)].append(word)

total = 0
for words in length_to_words.values():
    n = len(words)
    added = set()
    removed = set()
    for i in range(n):
        for j in range(i + 1, n):
            word_i = words[i]
            word_j = words[j]

            for k in range(len(word_i)):
                if word_i[k] != word_j[k]:
                    break

            if 0 <= k < len(word_i) - 1 and word_i[k + 1] != word_j[k + 1] and word_i[k + 2:] == word_j[k + 2:]:
                first, second = sorted([word_i[k:k+2], word_j[k:k+2]])
                pair = (first, second, k)
                if pair in added:
                    added.remove(pair)
                    removed.add(pair)
                elif pair not in removed:
                    added.add(pair)

    total += len(added)

print(total)