from functools import cache

MOD = int(1e9) + 7

n, l = list(map(int, input().split()))
word = input()

word_to_idx = {}
idx_to_word = {}
idx = 0

for i in range(len(word)):
    for j in range(i, len(word)):
        substr = word[i:j + 1]
        if substr not in word_to_idx:
            word_to_idx[substr] = idx
            idx_to_word[idx] = substr
            idx += 1

@cache
def get_substrs(word):
    substrs = set()
    for i in range(len(word)):
        for j in range(i, len(word)):
            substr = word[i:j + 1]
            substrs.add(word_to_idx[substr])
    return list(substrs)

for i in range(len(word)):
    for j in range(i, len(word)):
        get_substrs(word[i: j + 1])

word_to_children = [get_substrs(idx_to_word[i]) for i in range(idx)]
prev = [1] * idx

for _ in range(l):
    curr = [0] * idx
    for i in range(idx):
        curr[i] = sum(prev[child_id] for child_id in word_to_children[i]) % MOD
    prev = curr

print(prev[word_to_idx[word]])