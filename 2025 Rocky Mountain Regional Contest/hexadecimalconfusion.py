n = int(input())

mapping = {e: i for i, e in enumerate("0123456789ABCDEF")}

min_sum = 0
max_sum = 0

for _ in range(n):
    hexa = input()
    curr_low = 0
    curr_high = 0

    for i in range(len(hexa)):
        curr_low *= 16
        curr_high *= 16

        if hexa[i] == "0" or hexa[i] == "D":
            curr_high += mapping["D"]
            if i == 0 and len(hexa) != 1:
                curr_low += mapping["D"]
        elif hexa[i] == "B" or hexa[i] == "8":
            curr_low += mapping["8"]
            curr_high += mapping["B"]
        else:
            curr_low += mapping[hexa[i]]
            curr_high += mapping[hexa[i]]

    min_sum += curr_low
    max_sum += curr_high

print(hex(max_sum)[2:].upper())
print(hex(min_sum)[2:].upper())