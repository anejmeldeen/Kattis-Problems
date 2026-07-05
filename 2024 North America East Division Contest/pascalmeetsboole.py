import math

n = int(input())
for _ in range(n):
    data = input().split()
    code = data[0]
    query = data[1]
    row = int(data[2])
    index = -1
    if query == "B":
        index = int(data[3])

    # all one (covers 8 cases)
    if code[-1] == "1":
        if query == "N":
            print(row * (row + 1) // 2)
        else:
            print(1)
    elif code == "0000":
        if query == "N":
            print(row * 2 - 1)
        else:
            if index == 1 or index == row:
                print(1)
            else:
                print(0)
    elif code == "0010":
        if query == "N":
            row_num = math.ceil((row - 1) / 2) + 1
            row_num_minus = math.ceil((row - 2) / 2) + 1
            summy = row_num * (row_num + 1) // 2
            summy += row_num_minus * (row_num_minus + 1) // 2 - 1
            print(summy)
        else:
            if index == 1 or index == row:
                print(1)
            elif index % 2 == row % 2:
                print(1)
            else:
                print(0)
    elif code == "0100":
        if query == "N":
            row_num = math.ceil((row - 1) / 2) + 1
            row_num_minus = math.ceil((row - 2) / 2) + 1
            summy = row_num * (row_num + 1) // 2
            summy += row_num_minus * (row_num_minus + 1) // 2 - 1
            print(summy)
        else:
            if index == 1 or index == row:
                print(1)
            elif index % 2 == 1:
                print(1)
            else:
                print(0)
    elif code == "0110":
        def get_xorn(r):
            if r == 0:
                return 0
            if r == 1:
                return 1
            if r == 2:
                return 3
            if r == 3:
                return 5
            if r == 4:
                return 9
            powwy = 4
            summy = 9
            while powwy <= r:
                powwy *= 2
                summy *= 3
            powwy //= 2
            summy //= 3
            return summy + 2 * get_xorn(r % powwy)
        
        def get_xorb(r, i):
            if (i == 1 or i == r):
                return 1
            powwy = 2
            while powwy < r:
                powwy *= 2
            powwy //= 2
            new_r = r % powwy
            if new_r == 0:
                new_r = powwy
            if i > powwy:
                new_i = i - powwy
            else:
                new_i = i
            if new_i > new_r:
                return 0
            return get_xorb(new_r, new_i)
        
        if query == "N":
            print(get_xorn(row))
        else:
            print(get_xorb(row, index))

    elif code == "1000":
        if query == "N":
            summy = max(0, math.ceil((row - 4) / 2)) ** 2 + 2 * row - 1
            print(summy)
        else:
            if index == 1 or index == row:
                print(1)
            elif row % 2 == 0:
                print(0)
            else:
                if index == 2 or index == row - 1:
                    print(0)
                else:
                    print(1)
    elif code == "1010":
        if query == "N":
            row_num = math.ceil((row - 1) / 2) + 1
            row_num_minus = math.ceil((row - 2) / 2) + 1
            summy = row_num * (row_num + 1) // 2
            summy += row_num_minus * (row_num_minus + 1) // 2 - 1
            print(summy)
        else:
            if index == 1 or index == row:
                print(1)
            elif index % 2 == row % 2:
                print(1)
            else:
                print(0)
    elif code == "1100":
        if query == "N":
            row_num = math.ceil((row - 1) / 2) + 1
            row_num_minus = math.ceil((row - 2) / 2) + 1
            summy = row_num * (row_num + 1) // 2
            summy += row_num_minus * (row_num_minus + 1) // 2 - 1
            print(summy)
        else:
            if index == 1 or index == row:
                print(1)
            elif index % 2 == 1:
                print(1)
            else:
                print(0)
    elif code == "1110":
        if query == "N":
            row_down = row // 2
            row_up = math.ceil(row / 2)
            summy = row_down * (row_down + 1)
            summy += 2 * row_up - 1
            print(summy)
        else:
            if index == 1 or index == row:
                print(1)
            elif row % 2 == 1:
                print(0)
            else:
                print(1)