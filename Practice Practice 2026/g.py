string1 = input()
string2 = input()

substrs1 = set()
substrs2 = set()
for i in range(len(string1)):
    for j in range(i + 2, len(string1)):
        substrs1.add(string1[i:j+1])
for i in range(len(string2)):
    for j in range(i + 2, len(string2)):
        substrs2.add(string2[i:j+1])

allowed = substrs1 & substrs2
groups = set()

for word in allowed:
    groups.add(''.join(sorted(word)))

print(len(groups))