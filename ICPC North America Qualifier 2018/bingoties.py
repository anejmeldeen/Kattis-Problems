n = int(input())
cards = []

for i in range(n):
    card = []
    for _ in range(5):
        card.append(list(map(int, input().split())))
    if i != n - 1:
        input()
    cards.append(card)

for i in range(n):
    for j in range(i + 1, n):
        left_card = cards[i]
        right_card = cards[j]
        for left_row in left_card:
            for right_row in right_card:
                for left_num in left_row:
                    if left_num in right_row:
                        other_nums = set(left_row + right_row)
                        other_nums.discard(left_num)
                        allowed = True
                        for card in cards:
                            for row in card:
                                has_all = True
                                for ele in row:
                                    if ele not in other_nums:
                                        has_all = False
                                if has_all:
                                    allowed = False
                        if allowed:
                            print(i + 1, j + 1)
                            exit()
print("no ties")