t = int(input())
mini = float('inf')
curr = 0
for _ in range(t):
    curr += int(input())
    mini = min(mini, curr)

print(-mini if mini < 0 else 0)