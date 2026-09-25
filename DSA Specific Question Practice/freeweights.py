n = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

left = 0
right = max(max(row1), max(row2))
while left <= right:
    mid = (left + right) // 2
    stack = []

    possible = True
    for ele in row1:
        if ele <= mid:
            continue
        if stack and stack[-1] != ele:
            possible = False
        elif stack and stack[-1] == ele:
            stack.pop()
        else:
            stack.append(ele)
    if stack:
        possible = False
    stack = []
    for ele in row2:
        if ele <= mid:
            continue
        if stack and stack[-1] != ele:
            possible = False
        elif stack and stack[-1] == ele:
            stack.pop()
        else:
            stack.append(ele)
    if stack:
        possible = False

    if possible:
        right = mid - 1
    else:
        left = mid + 1

print(left)