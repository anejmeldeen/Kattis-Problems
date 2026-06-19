from collections import deque

queue = deque()
queue.append(([[".", ".", "."], [".", ".", "."], [".", ".", "."]], 0))

hashy = {}
hashy["........."] = 0

sol = -1
while queue:
    curr, count = queue.popleft()

    for x in range(3):
        for y in range(3):
            new = []
            for row in curr:
                new.append(row.copy())
            new[x][y] = "*" if curr[x][y] == "." else "."
            if x > 0:
                new[x - 1][y] = "*" if new[x - 1][y] == "." else "."
            if y > 0:
                new[x][y - 1] = "*" if curr[x][y - 1] == "." else "."
            if x < 2:
                new[x + 1][y] = "*" if curr[x + 1][y] == "." else "."
            if y < 2:
                new[x][y + 1] = "*" if curr[x][y + 1] == "." else "."

            code = ""
            for arr in new:
                for char in arr:
                    code += char
            if code in hashy:
                continue
            
            hashy[code] = count + 1
            queue.append((new, count + 1))

t = int(input())
for _ in range(t):
    end_code = ""
    for _ in range(3):
        end_code += input()

    print(hashy[end_code])