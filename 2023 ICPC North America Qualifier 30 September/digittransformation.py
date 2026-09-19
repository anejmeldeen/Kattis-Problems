string = input()
n = len(string)

nums = set(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])

stack = []
dp = [0] * (n + 1)
ways = [0] * (n + 1)
ways[0] = 1
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    ways[i] = ways[i - 1]
    stack.append(string[i - 1])
    for num in nums:
        length = len(num)
        start = i - length
        if start >= 0 and string[start:i] == num:
            value = length - 1 + dp[start]
            if value > dp[i]:
                dp[i] = value
                ways[i] = ways[start]
            elif value == dp[i]:
                ways[i] += ways[start]
                ways[i] %= 9302023

print(len(stack) - dp[-1])
print(ways[-1])