n, m, a, c, x0 = list(map(int, input().split()))

sequence = []
for _ in range(n):
    x0 = (a * x0 + c) % m
    sequence.append(x0)

found = set()

def recurse(left, right, mini=float('-inf'), maxi=float('inf')):
    if left > right or mini > maxi:
        return
    mid = (left + right) // 2
    if mini <= sequence[mid] <= maxi:
        found.add(sequence[mid])
    recurse(left, mid - 1, mini, min(maxi, sequence[mid]))
    recurse(mid + 1, right, max(mini, sequence[mid]), maxi)

recurse(0, len(sequence) - 1)
print(len(found))