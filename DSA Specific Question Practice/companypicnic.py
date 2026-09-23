n = int(input())
graph = {}
ceo = -1

name_to_speed = {}
for _ in range(n):
    data = input().split()
    name, speed, manager = data
    speed = float(speed)
    if manager == "CEO":
        ceo = name
    else:
        if manager not in graph:
            graph[manager] = []
        if name not in graph:
            graph[name] = []
        graph[manager].append(name)
    name_to_speed[name] = speed

def dfs(node):
    choices = []
    for child in graph[node]:
        choices.append(dfs(child))

    dfs_exclude_len = 0
    dfs_exclude_total = 0
    for choice in choices:
        use = max(choice)
        dfs_exclude_len += use[0]
        dfs_exclude_total += use[1]

    include_use = (0, 0)
    len_of_children = 0
    sum_of_children = 0
    for i in range(len(choices)):
        best = max(choices[i])
        len_of_children += best[0]
        sum_of_children += best[1]

    for i in range(len(choices)):
        dfs_include_len = len_of_children + choices[i][0][0] + 1
        dfs_include_total = sum_of_children + choices[i][0][1] + min(name_to_speed[node], name_to_speed[graph[node][i]])

        best = max(choices[i])
        dfs_include_len -= best[0]
        dfs_include_total -= best[1]
        trial = (dfs_include_len, dfs_include_total)

        if trial > include_use:
            include_use = trial

    return [(dfs_exclude_len, dfs_exclude_total), include_use]
    

arr = dfs(ceo)
use = max(arr)

print(f"{use[0]} {use[1] / use[0]}")