number = int(input())

cost_to_set = {}
cost_to_set[1] = set([1])

sol = -1
if number == 1:
    sol = 1

curr_cost = 2
while True and sol == -1:
    new_set = set()
    for i in range(1, curr_cost // 2 + 1):
        set_1 = cost_to_set[i]
        set_2 = cost_to_set[curr_cost - i]

        for ele1 in set_1:
            for ele2 in set_2:
                res1 = int(str(ele1) + str(ele2))
                res2 = int(str(ele2) + str(ele1))
                res3 = ele1 + ele2
                res4 = ele1 * ele2
                res = [res1, res2, res3, res4]
                for item in res:
                    if item <= 100000:
                        new_set.add(item)

    if number in new_set:
        sol = curr_cost
        break

    cost_to_set[curr_cost] = new_set
    curr_cost += 1

print(sol)