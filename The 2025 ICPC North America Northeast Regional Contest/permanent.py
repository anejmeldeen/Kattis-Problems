n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

def solve(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    n = len(matrix)
    total = 0
    for j in range(n):
        mult = matrix[0][j]
        new_matrix = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if j == k:
                    continue
                row.append(matrix[i][k])
            new_matrix.append(row)
        total += mult * solve(new_matrix)
    return total

print(solve(matrix))