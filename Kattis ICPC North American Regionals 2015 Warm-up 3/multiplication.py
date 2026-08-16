while (data := input()) != "0 0":
    data = data.split()
    h, v = len(data[0]), len(data[1])
    a, b = int(data[0]), int(data[1])

    product = a * b
    str_product = str(product)
    str_product = (h + v - len(str_product)) * " " + str_product
    idx = 0

    print("+" + (h * 3 + h + 3) * "-" + "+")
    line_1 = "|  " + ' '.join([" " + data[0][i] + " " for i in range(h)]) + "  |"
    print(line_1)
    print("| " + "+" + "---+" * h + " |")
    for i, nummy in enumerate(data[1]):
        digit = int(nummy)
        board = []
        nums = []
        for char in data[0]:
            first_dig = int(char)
            res = first_dig * digit
            str_res = str(res)
            if len(str_res) == 1:
                str_res = "0" + str_res
            nums.append(str_res)
        board.append("|" + ("/" if i != 0 and str_product[i - 1] != " " else " ") + "|" + '|'.join([nums[i][0] + " /" for i in range(len(nums))]) + "| |")
        board.append("| |" + " / |" * h + nummy + "|")
        board.append("|" + str_product[idx] + "|" + '|'.join(["/ " + nums[i][1] for i in range(len(nums))]) + "| |")
        idx += 1

        board.append("| " + "+" + "---+" * h + " |")
        for row in board:
            print(''.join(row))
    print("|" + ("/" if idx != 0 and str_product[idx - 1] != " " else " ") + " " + " / ".join([x for x in str_product[idx:]]) + "    |")
    print("+" + (h * 3 + h + 3) * "-" + "+")

