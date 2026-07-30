n = int(input())
hills = list(map(int, input().split()))

maxi_here = [0] * n
maxi_rev = [0] * n

stack = []
for i, ele in enumerate(hills):
    if stack and ele < stack[-1]:
        stack = []
    stack.append(ele)
    maxi_here[i] = ele - stack[0]

stack = []
for i in range(n - 1, -1, -1):
    ele = hills[i]
    if stack and ele < stack[-1]:
        stack = []
    stack.append(ele)
    maxi_rev[i] = ele - stack[0]

print(max(min(maxi_here[i], maxi_rev[i]) for i in range(n)))