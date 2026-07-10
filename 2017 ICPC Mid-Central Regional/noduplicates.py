words = input().split()

if len(words) == len(set(words)):
    print("yes")
else:
    print("no")