string = input()
count = 0
idx = 0
go_up = True
works = True
while idx < len(string):
    if go_up:
        if string[idx] == "|":
            count += 1
        elif string[idx] == "(":
            if idx + 1 < len(string) and string[idx + 1] == ")":
                idx += 1
                go_up = False
            else:
                works = False
                break
        else:
            works = False
            break
    else:
        if string[idx] == "|":
            count -= 1
        else:
            works = False
            break
    idx += 1

if works and count == 0:
    print("correct")
else:
    print("fix")