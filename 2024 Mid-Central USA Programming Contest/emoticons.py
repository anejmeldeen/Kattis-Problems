emojis = set([":)", ":-)", ":-(", ";-)", "xD", "^_^", "-_-", "^o^", "^^;", "(..)"])
chars = " 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
string = input()

mini = float('inf')
maxi = float('-inf')
for char_from in chars:
    for char_to in chars:
        stack = []
        for char in string:
            if char == char_from:
                stack.append(char_to)
            else:
                stack.append(char)

            if len(stack) >= 2:
                prev2 = ''.join(stack[-2:])
                if prev2 in emojis:
                    stack.pop()
                    stack.pop()
                    stack.append("A")
            if len(stack) >= 3:
                prev3 = ''.join(stack[-3:])
                if prev3 in emojis:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append("A")
            if len(stack) >= 4:
                prev4 = ''.join(stack[-4:])
                if prev4 in emojis:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append("A")

        mini = min(mini, len(stack))
        maxi = max(maxi, len(stack))

print(mini, maxi)