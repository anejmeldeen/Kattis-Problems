num_ww, num_wb, num_bw, num_bb, l = list(map(int, input().split()))

blacks = set()
whites = set()
for i in range(1, 89):
    if i % 12 in [0, 2, 5, 7, 10]:
        blacks.add(i)
    else:
        whites.add(i)

ww = {}
wb = {}
bw = {}
bb = {}

def gather_data(count, dictionary):
    for _ in range(count):
        data = list(map(int, input().split()))
        key = (data[0], data[1])
        dictionary[key] = data[2:]

gather_data(num_ww, ww)
gather_data(num_wb, wb)
gather_data(num_bw, bw)
gather_data(num_bb, bb)

nums = list(map(int, input().split()))
dp = [[float('inf')] * l for _ in range(5)]
for finger in range(5):
    dp[finger][0] = 0

for i in range(1, l):
    prev_note = nums[i - 1]
    note = nums[i]

    reverse = False
    steps = note - prev_note
    if steps < 0:
        reverse = True
        steps = -steps

    left_white = min(note, prev_note) in whites
    right_white = max(note, prev_note) in whites

    if left_white and right_white:
        dictionary = ww
    elif left_white and not right_white:
        dictionary = wb
    elif not left_white and right_white:
        dictionary = bw
    else:
        dictionary = bb

    if steps == 0:
        for finger in range(5):
            dp[finger][i] = dp[finger][i - 1]
    else:
        for curr_finger in range(5):
            for prev_finger in range(5):
                if prev_finger == curr_finger:
                    continue

                if reverse:
                    key = (curr_finger + 1, prev_finger + 1)
                else:
                    key = (prev_finger + 1, curr_finger + 1)

                if key in dictionary:
                    add_cost = dictionary[key][steps - 1]
                    dp[curr_finger][i] = min(dp[curr_finger][i], dp[prev_finger][i - 1] + add_cost)

print(min([dp[x][-1] for x in range(5)]))