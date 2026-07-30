n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input().split())

if n >= 3:
    first_len = (len(matrix[0][1]) + len(matrix[0][2]) - len(matrix[1][2])) // 2
    if first_len <= 0:
        print("NONE")
        exit()

    words = [matrix[0][1][:first_len]]

    for i in range(1, n):
        new_word = matrix[0][i][first_len:]
        if len(new_word) <= 0:
            print("NONE")
            exit()
        words.append(matrix[0][i][first_len:])

    new_matrix = [["*"] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                new_matrix[i][j] = words[i] + words[j]

    valid = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != new_matrix[i][j]:
                valid = False

    if valid:
        print("UNIQUE")
        for word in words:
            print(word)
    else:
        print("NONE")
else:
    def nEquals2Case(string1, string2):
        mod = int(1e9+7)
        hash1 = 0
        hash2 = 0
        values1 = set()
        vals = []

        count = 0

        if len(string1) != len(string2):
            return "NONE", None

        for i in range(len(string1)-1):
            hash1 = (hash1 * 27 + (ord(string1[i])-96)) % mod
            hash2 = (hash2 + (ord(string2[len(string2)-1-i])-96)*(pow(27, i, mod))) % mod
            if hash1 == hash2:
                values1.add(i)
        hash1 = 0
        hash2 = 0

        for i in range(len(string1)-1):
            hash1 = (hash1 * 27 + (ord(string2[i])-96)) % mod
            hash2 = (hash2 + (ord(string1[len(string1)-1-i])-96)*(pow(27, i, mod))) % mod
            if hash1 == hash2 and len(string1)-2-i in values1:
                count += 1
                vals.append(len(string1)-2-i)
        if count == 0:
            return "NONE", None
        if count == 1:
            return "UNIQUE", vals[0]
        return "MANY", None
    vals = nEquals2Case(matrix[0][1], matrix[1][0])
    if vals[0] != "UNIQUE":
        print(vals[0])
    else:
        print(vals[0])
        print(matrix[0][1][:vals[1] + 1])
        print(matrix[0][1][vals[1] + 1:])