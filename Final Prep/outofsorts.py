n, m, a, c, x0 = list(map(int, input().split()))

arr = []
for _ in range(n):
    x0 = (a * x0 + c) % m
    arr.append(x0)

left = 0
right = len(arr) - 1
works = set()
def solve(left, right, mini=float('-inf'), maxi=float('inf')):
    if left > right:
        return
    mid = (left + right) // 2
    if mini <= arr[mid] <= maxi:
        works.add(arr[mid])
    solve(mid + 1, right, max(arr[mid], mini), maxi)
    solve(left, mid - 1, mini, min(arr[mid], maxi))

solve(left, right)
print(len(works))