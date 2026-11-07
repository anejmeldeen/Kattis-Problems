sequence = input()
n = len(sequence)
m = int(input())

a_fix = [0] * (n + 1)
g_fix = [0] * (n + 1)
t_fix = [0] * (n + 1)
c_fix = [0] * (n + 1)
for i in range(1, n + 1):
    a_fix[i] = a_fix[i - 1] + (sequence[i - 1] == "A")
    c_fix[i] = c_fix[i - 1] + (sequence[i - 1] == "C")
    t_fix[i] = t_fix[i - 1] + (sequence[i - 1] == "T")
    g_fix[i] = g_fix[i - 1] + (sequence[i - 1] == "G")

for _ in range(m):
    left, right = list(map(int, input().split()))
    arr = [(t_fix[right] - t_fix[left - 1], 3, "T"), (c_fix[right] - c_fix[left - 1], 1, "C"), (g_fix[right] - g_fix[left - 1], 2, "G"), (a_fix[right] - a_fix[left - 1], 4, "A")]
    arr.sort(reverse=True)
    res = arr[0][2] + arr[1][2] + arr[2][2] + arr[3][2]
    print(res)