hp, wp, hm, wm = list(map(int, input().split()))
HORIZ_BASE = 31
VERT_BASE = 37
MOD = 10 ** 9 + 7

painting = []
masterpiece = []
for _ in range(hp):
    painting.append(input())
for _ in range(hm):
    masterpiece.append(input())

base_pow_wp = pow(HORIZ_BASE, wp - 1, MOD)
base_pow_hp = pow(VERT_BASE, hp - 1, MOD)
def roll_hash(curr_hash, left_char, right_char, base_pow, base):
    if left_char != 0:
        curr_hash -= left_char * base_pow
    curr_hash *= base
    curr_hash += right_char
    curr_hash %= MOD
    return curr_hash

row_hashes = []
for row in painting:
    curr_hash = 0
    for char in row:
        val = 1 if char == "o" else 2
        curr_hash = roll_hash(curr_hash, 0, val, base_pow_wp, HORIZ_BASE)
    row_hashes.append(curr_hash)
key_hash = 0
for row_hash in row_hashes:
    key_hash = roll_hash(key_hash, 0, row_hash, base_pow_hp, VERT_BASE)

hashed_matrix = [[] for _ in range(hm)]
for j, row in enumerate(masterpiece):
    curr_hash = 0
    for i, char in enumerate(row):
        val = 1 if char == "o" else 2
        prev_val = 0
        if i >= wp:
            prev_val = 1 if row[i - wp] == "o" else 2
        curr_hash = roll_hash(curr_hash, prev_val, val, base_pow_wp, HORIZ_BASE)
        if i >= wp - 1:
            hashed_matrix[j].append(curr_hash)

final_count = 0
for j in range(wm - wp + 1):
    col = [hashed_matrix[i][j] for i in range(hm)]
    curr_hash = 0
    for j, val in enumerate(col):
        prev_val = 0
        if j >= hp:
            prev_val = col[j - hp]
        curr_hash = roll_hash(curr_hash, prev_val, val, base_pow_hp, VERT_BASE)
        if j >= hp - 1:
            final_count += curr_hash == key_hash

print(final_count)