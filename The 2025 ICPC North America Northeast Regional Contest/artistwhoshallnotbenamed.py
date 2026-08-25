n = int(input())
boring = cool = artistic = 0

names = []
for _ in range(n):
    names.append(input())

mappy = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000",
         "9": "1001", "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110", "f": "1111"}

for name in names:
    if len(name) % 2 != 0:
        artistic += 1
        continue
    valid = True
    interesting = False

    idx = 0
    is_multi = 0
    curr = ""
    while idx < len(name):
        nibble = name[idx:idx + 2]
        num = mappy[nibble[0]] + mappy[nibble[1]]
        if is_multi:
            if num[:2] != "10":
                valid = False
                break
            is_multi -= 1
            interesting = True
            curr += num[2:]
        elif num[:3] == "110":
            is_multi = 1
            curr += num[3:]
        elif num[:4] == "1110":
            is_multi = 2
            curr += num[4:]
        elif num[:5] == "11110":
            is_multi = 3
            curr += num[5:]
        elif num[0] != "0":
            valid = False
            break
        else:
            curr += num[1:]
        if is_multi == 0:
            curr = int(curr, 2)
            if 0xD800 <= curr <= 0xDFFF or 0xFDD0 <= curr <= 0xFDEF or curr == 0xFFFE or curr == 0xFFFF:
                valid = False
                break
            curr = ""
        idx += 2
    if is_multi:
        valid = False
    if not valid:
        artistic += 1
    elif interesting:
        cool += 1
    else:
        boring += 1

print(boring, cool, artistic)