n = int(input())
words = []
for _ in range(n):
    words.append(input())

smallest = float('inf')
last_seen = {}
for i, word in enumerate(words):
    if word in last_seen:
        smallest = min(smallest, i - last_seen[word])
    last_seen[word] = i

print((n - smallest) if smallest != float('inf') else 0)