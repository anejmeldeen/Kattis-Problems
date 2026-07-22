data = list(map(int, input().split()))
nums = data[:6]
tower1 = data[6]
first = []
second = []

for binary in range(1 << 6):
    one_count = 0
    temp = binary
    while temp > 0:
        one_count += temp & 1
        temp >>= 1
    if one_count != 3:
        continue
    sum1 = 0
    curr_first = []
    curr_second = []
    for i in range(6):
        if binary & 1:
            sum1 += nums[i]
            curr_first.append(nums[i])
        else:
            curr_second.append(nums[i])
        binary >>= 1
    if sum1 == tower1:
        first = curr_first
        second = curr_second

first.sort(reverse=True)
second.sort(reverse=True)
print(' '.join(list(map(str, first + second))))