n = int(input())
first = input()
second = input()

dist = 0
for i in range(n):
    char1 = first[i]
    char2 = second[i]
    straight = abs(ord(char1) - ord(char2))
    wrap1 = ord(char1) - ord('A') + ord('Z') - ord(char2) + 1
    wrap2 = ord(char2) - ord('A') + ord('Z') - ord(char1) + 1
    dist += min(straight, wrap1, wrap2)

print(dist)