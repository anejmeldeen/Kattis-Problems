words = input().split()
word1, word2 = words[0], words[1]

diffs = []
for i in range(len(word1)):
    diffs.append(ord(word1[i]) - ord(word2[i]))

last = 0
total = 0
for diff in diffs:
    item = min(abs(diff), max(abs(last) - abs(diff), 0))
    total += item
    last = diff

print(total)