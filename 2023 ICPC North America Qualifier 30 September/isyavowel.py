string = input()
vowels = ["a", "e", "i", "o", "u", "y"]
counts = []

for vowel in vowels:
    counts.append(string.count(vowel))

print(sum(counts[:-1]), sum(counts))