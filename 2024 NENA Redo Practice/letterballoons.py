letters, teams = list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

allowed_chars = set(alpha[:letters])

words = []
for _ in range(teams):
    string = input()
    works = True
    if len(set(string)) != len(string):
        works = False
    for char in string:
        if char not in allowed_chars:
            works = False
    if works:
        words.append(string)

word_nums = []
for word in words:
    mask = 0
    for char in word:
        dist = ord(char) - ord('A')
        mask |= (1 << dist)
    word_nums.append(mask)

best = 0
for trial in range(1 << len(word_nums)):
    use = []
    works = True
    count = 0
    for word_num in word_nums:
        if trial & 1:
            use.append(word_num)
            count += 1
        trial >>= 1

    mask = 0
    for num in use:
        if mask & num > 0:
            works = False
        mask |= num

    if works:
        best = max(best, count)

print(best)