language = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
char_to_int = {e: i for i, e in enumerate(language)}
int_to_char = {i: e for i, e in enumerate(language)}
while (data := input()) != "0":
    rotations, word = data.split()
    rotations = int(rotations)
    word = word[::-1]
    res = []
    for char in word:
        idx = char_to_int[char]
        idx += rotations
        idx %= 28
        res.append(int_to_char[idx])

    print(''.join(res))