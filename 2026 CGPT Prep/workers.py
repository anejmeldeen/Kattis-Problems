n = int(input())

INF = int(1e18)

def hungarian(raw_matrix):
    number_of_workers = len(raw_matrix)
    number_of_jobs = len(raw_matrix[0])
    cost_matrix = [[0] * (number_of_jobs + 1)] + [[0] + row for row in raw_matrix]
    row_potential = [0] * (number_of_workers + 1)
    column_potential = [0] * (number_of_jobs + 1)
    job_assignment = [0] * (number_of_jobs + 1)
    previous_column = [0] * (number_of_jobs + 1)
    for worker_index in range(1, number_of_workers + 1):
        job_assignment[0] = worker_index
        current_column = 0
        minimum_slack = [INF] * (number_of_jobs + 1)
        visited_columns = [False] * (number_of_jobs + 1)
        while True:
            visited_columns[current_column] = True
            current_worker = job_assignment[current_column]
            delta_value = INF
            next_column = 0
            for job_index in range(1, number_of_jobs + 1):
                if not visited_columns[job_index]:
                    current_slack = cost_matrix[current_worker][job_index] - row_potential[current_worker] - column_potential[job_index]
                    
                    if current_slack < minimum_slack[job_index]:
                        minimum_slack[job_index] = current_slack
                        previous_column[job_index] = current_column
                    
                    if minimum_slack[job_index] < delta_value:
                        delta_value = minimum_slack[job_index]
                        next_column = job_index
            for job_index in range(number_of_jobs + 1):
                if visited_columns[job_index]:
                    row_potential[job_assignment[job_index]] += delta_value
                    column_potential[job_index] -= delta_value
                else:
                    minimum_slack[job_index] -= delta_value

            current_column = next_column
            if job_assignment[current_column] == 0:
                break

        while True:
            next_column = previous_column[current_column]
            job_assignment[current_column] = job_assignment[next_column]
            current_column = next_column
            if current_column == 0:
                break
    
    return -column_potential[0], job_assignment

gate_cost = []
work_station_cost = []

for _ in range(n):
    data = list(map(int, input().split()))
    arr = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    gate_cost.append(arr)
for _ in range(n):
    data = list(map(int, input().split()))
    arr = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    work_station_cost.append(arr)

best = float('inf')
best_arr = -1
row1 = []
row2 = []
for arrangement in range(n + 1):
    key = [0] * (n - arrangement) + [1] * (arrangement)
    real_cost = []
    real_work_cost = []
    for arr in gate_cost:
        real_cost.append([arr[i][key[i]] for i in range(n)])
    for arr in work_station_cost:
        real_work_cost.append([arr[i][key[i]] for i in range(n)])

    hung1 = hungarian(real_cost)
    hung2 = hungarian(real_work_cost)
    cost = hung1[0] + hung2[0]
    if cost < best:
        best = cost
        best_arr = key
        row1 = hung1[1]
        row2 = hung2[1]

print(best)
res = [None] * n

for gate in range(1, n + 1):
    char = "A" if (best_arr[gate - 1] == 0) else "B"
    res[row1[gate] - 1] = f"{row1[gate]} {gate}{char} {row2[gate]}"

for item in res:
    print(item)