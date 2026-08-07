t = int(input())
translation = {e: i for i, e in enumerate(" abcdefghijklmnopqrstuvwxyz")}
rev_translation = {i: e for i, e in enumerate(" abcdefghijklmnopqrstuvwxyz")}

for _ in range(t):
    data = input()

    if data[0] == "e":
        nums = []
        for char in data[2:]:
            nums.append(translation[char])
        new_nums = []
        for i in range(len(nums)):
            if i == 0:
                new_nums.append(nums[i])
            else:
                prev = new_nums[i - 1]
                new_nums.append(nums[i] + new_nums[i - 1])
                new_nums[i] %= 27

        res = ""
        for num in new_nums:
            res += rev_translation[num]

        print(res)

    else:
        nums = []
        for char in data[2:]:
            nums.append(translation[char])
        new_nums = []

        for i in range(len(nums)):
            if i == 0:
                new_nums.append(nums[i])
            else:
                new_nums.append(nums[i] - nums[i - 1])
                new_nums[i] %= 27

        res = ""
        for num in new_nums:
            res += rev_translation[num]

        print(res)