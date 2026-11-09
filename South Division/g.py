word = input()

valid = set(word)

left = 0
for right in range(len(word)):
    if word[right] != word[left]:
        if left > 0 and word[left - 1] != word[right]:
            valid.discard(word[left])
        left = right

sol = []
for ele in valid:
    sol.append(ele)
print(''.join(sorted(sol)))