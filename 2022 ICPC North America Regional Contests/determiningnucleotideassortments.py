string = input()
n = len(string)
m = int(input())

t_pref = [0] * (n + 1)
a_pref = [0] * (n + 1)
g_pref = [0] * (n + 1)
c_pref = [0] * (n + 1)

for i in range(1, n + 1):
    t_pref[i] = t_pref[i - 1] + (string[i - 1] == "T")
    a_pref[i] = a_pref[i - 1] + (string[i - 1] == "A")
    g_pref[i] = g_pref[i - 1] + (string[i - 1] == "G")
    c_pref[i] = c_pref[i - 1] + (string[i - 1] == "C")

for _ in range(m):
    left, right = list(map(int, input().split()))
    t_count = t_pref[right] - t_pref[left - 1]
    a_count = a_pref[right] - a_pref[left - 1]
    g_count = g_pref[right] - g_pref[left - 1]
    c_count = c_pref[right] - c_pref[left - 1]

    res = [(-t_count, "T"), (-a_count, "A"), (-g_count, "G"), (-c_count, "C")]

    def order(tuppy):
        mappy = {"T": 1, "A": 0, "G": 2, "C": 3}
        return tuppy[0] * 100 + mappy[tuppy[1]]
    res.sort(key=order)

    ans = ""
    for item in res:
        ans += item[1]

    print(ans)