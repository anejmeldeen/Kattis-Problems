t = int(input())
for _ in range(t):
    string = input()
    possible = False
    for end in range(min(7, len(string))):
        works = True
        start = 0
        while True:
            setty = set()
            for i in range(start, end):
                if string[i] in setty:
                    works = False
                    break
                setty.add(string[i])
            if end == len(string):
                break
            start = end
            end = min(end + 7, len(string))

        if works:
            possible = True

    if possible:
        print(1)
    else:
        print(0)