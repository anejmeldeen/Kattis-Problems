import heapq

n, m = list(map(int, input().split()))
city_storage = {}

for i in range(n):
    city_storage[i] = list(map(int, input().split()))

graph = {}
for i in range(n):
    locs = list(map(int, input().split()))
    graph[i] = []
    for j in range(n):
        if i == j or locs[j] == -1:
            continue
        graph[i].append((locs[j], j))

new_graph = {}
for start_node in range(n):
    costs = [float('inf')] * n
    heap = [(0, start_node)]
    seen = set()
    while heap:
        data = heapq.heappop(heap)
        curr_cost = data[0]
        curr_loc = data[1]

        seen.add(curr_loc)
        costs[curr_loc] = min(costs[curr_loc], curr_cost)

        for conn in graph[curr_loc]:
            if conn[1] in seen:
                continue
            conn_cost = conn[0]
            conn_loc = conn[1]
            heapq.heappush(heap, (curr_cost + conn_cost, conn_loc))
    new_graph[start_node] = costs

graph = new_graph

matrix = []
for city in range(n):
    costs = []
    for item in range(m):
        cost = 0
        for other_city in range(n):
            if city == other_city:
                continue
            amt = city_storage[other_city][item]
            cost += amt * graph[other_city][city]
        costs.append(cost)
    for _ in range(n - m):
        costs.append(0)
    matrix.append(costs)

#######################
# hungarian algorithm #
#######################

def hungarian_min_cost(raw_matrix):
    """
    Plug-and-play Hungarian Algorithm.
    Pass a standard 0-indexed NxM matrix (N workers <= M jobs).
    Returns the minimum cost to assign all N workers.
    """
    INF = float('inf')
    num_workers = len(raw_matrix)
    num_jobs = len(raw_matrix[0])
    
    # Pad matrix to 1-indexed internally for the math to work smoothly
    cost_matrix = [[0] * (num_jobs + 1)] + [[0] + row for row in raw_matrix]
    
    row_potential = [0] * (num_workers + 1)
    col_potential = [0] * (num_jobs + 1)
    job_match = [0] * (num_jobs + 1)
    prev_col = [0] * (num_jobs + 1)
    
    for worker in range(1, num_workers + 1):
        job_match[0] = worker
        current_col = 0
        min_slack = [INF] * (num_jobs + 1)
        visited_cols = [False] * (num_jobs + 1)
        
        while True:
            visited_cols[current_col] = True
            current_worker = job_match[current_col]
            delta = INF
            next_col = 0
            
            for job in range(1, num_jobs + 1):
                if not visited_cols[job]:
                    current_slack = cost_matrix[current_worker][job] - row_potential[current_worker] - col_potential[job]
                    
                    if current_slack < min_slack[job]:
                        min_slack[job] = current_slack
                        prev_col[job] = current_col
                        
                    if min_slack[job] < delta:
                        delta = min_slack[job]
                        next_col = job
                        
            for job in range(num_jobs + 1):
                if visited_cols[job]:
                    row_potential[job_match[job]] += delta
                    col_potential[job] -= delta
                else:
                    min_slack[job] -= delta
            
            current_col = next_col
            if job_match[current_col] == 0:
                break
                
        # Backtrack to apply the augmenting path
        while True:
            next_col = prev_col[current_col]
            job_match[current_col] = job_match[next_col]
            current_col = next_col
            if current_col == 0:
                break
                
    return -col_potential[0]

print(hungarian_min_cost(matrix))