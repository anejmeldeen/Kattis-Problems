n = int(input())
words = []
for _ in range(n):
    words.append(input())
set_words = set(words)

prefix = {}
for word in words:
    pref = word[:2]
    if pref in prefix:
        prefix[pref].add(word[2])
    else:
        prefix[pref] = set([word[2]])

counts = 0
for first in words:
    for second in words:
        chars = set()
        for char in first:
            chars.add(char)
        for char in second:
            chars.add(char)
        if len(chars) != 6:
            continue

        col1 = first[0] + second[0]
        col2 = first[1] + second[1]
        col3 = first[2] + second[2]
        diag1 = first[0] + second[1]
        diag2 = first[2] + second[1]

        if col1 not in prefix or col2 not in prefix or col3 not in prefix or diag1 not in prefix or diag2 not in prefix:
            continue

        first_poss = (prefix[col1] & prefix[diag2]).difference(chars)
        second_poss = (prefix[col2]).difference(chars)
        third_poss = (prefix[col3] & prefix[diag1]).difference(chars)

        for char1 in first_poss:
            for char2 in second_poss:
                if char2 == char1:
                    continue
                for char3 in third_poss:
                    if char3 == char2 or char3 == char1:
                        continue
                    if char1 + char2 + char3 in set_words:
                        counts += 1

print(counts)