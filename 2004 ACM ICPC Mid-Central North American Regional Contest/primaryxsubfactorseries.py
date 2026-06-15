import sys
sys.setrecursionlimit(int(1e9))

def find_subfactors(n):
    subfacs = []
    n = str(n)
    for mask in range(1, (1 << len(n)) - 1):
        old_mask = mask
        dig = ""
        idx = len(n) - 1
        while (mask > 0):
            if mask & 1:
                dig = n[idx] + dig
            mask >>= 1
            idx -= 1
        if dig[0] != "0" and int(n) % int(dig) == 0 and int(dig) != 1:
            modification = ""
            mask = old_mask
            idx = len(n) - 1
            for _ in range(len(n)):
                if not (mask & 1):
                    modification = n[idx] + modification
                mask >>= 1
                idx -= 1
            subfacs.append(int(modification))

    return subfacs

while (n := int(input())) != 0:
    sol = []

    def dfs(curr_num, path):
        path.append(curr_num)
        subfacs = find_subfactors(curr_num)
        best_path = []
        for subfac in set(subfacs):
            new_path = path.copy()
            res_path = dfs(subfac, new_path)
            if len(res_path) > len(best_path):
                best_path = res_path
            if len(res_path) == len(best_path) and res_path < best_path:
                best_path = res_path
        if not best_path:
            return path
        return best_path

    arr = []
    print(' '.join(list(map(str, dfs(n, arr)))))