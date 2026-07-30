import math
n = int(input())

alice = 0
bob = 0
works = True
rounds = 0

inputs = []
for _ in range(n):
    inputs.append(input())

for i, data in enumerate(inputs):
    text = data.split("-")
    num1 = int(text[0])
    num2 = int(text[1])

    total = alice + bob
    new_total = num1 + num2

    diff = new_total - total
    if diff < 0:
        works = False
        print(f"error {i + 1}")
        break
    else:
        if diff > 0 and (alice >= 11 or bob >= 11):
            works = False
            print(f"error {i + 1}")
            break

        rounds += diff
        if math.ceil(rounds / 2) % 2 == 0:
            alice_curr = num1
            bob_curr = num2
        else:
            alice_curr = num2
            bob_curr = num1

        if alice > alice_curr or bob > bob_curr or (alice_curr == 11 and bob_curr == 11) or alice_curr > 11 or bob_curr > 11:
            print(f"error {i + 1}")
            works = False
            break

        alice = alice_curr
        bob = bob_curr

if works:
    print("ok")