t = int(input())
for _ in range(t):
    x_arm, x_leg, y_arm, y_leg, total_arm, total_leg = list(map(int, input().split()))

    sols = 0
    x = -1
    y = -1

    for i in range(1, total_arm // x_arm + 1):
        arm_count = x_arm * i
        leg_count = x_leg * i

        j = (total_arm - arm_count) // y_arm

        if arm_count + j * y_arm == total_arm and leg_count + j * y_leg == total_leg and j != 0:
            sols += 1
            x = i
            y = j

    print(f"{x} {y}" if sols == 1 else "?")