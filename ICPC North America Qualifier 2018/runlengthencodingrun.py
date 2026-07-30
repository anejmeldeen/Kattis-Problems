do, word = input().split()

if do == "E":
    count = 1
    new_str = ""
    prev = -1
    for char in word:
        if char != prev:
            if prev != -1:
                new_str += prev + str(count)
                count = 1
        else:
            count += 1
        prev = char
    print(new_str + prev + str(count))
elif do == "D":
    new_str = ""
    for i in range(0, len(word), 2):
        char = word[i]
        num = int(word[i + 1])
        new_str += num * char
    print(new_str)