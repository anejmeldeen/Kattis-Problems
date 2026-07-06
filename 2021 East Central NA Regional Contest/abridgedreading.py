n, m = list(map(int, input().split()))
arr = []
while len(arr) < n:
    arr += list(map(int, input().split()))

graph = {}
culminate = set([x for x in range(1, n + 1)])
for _ in range(m):
    x, y = list(map(int, input().split()))
    if y not in graph:
        graph[y] = []
    graph[y].append(x)
    culminate.discard(x)

def recurse(num, setty):
    setty.add(num)
    if num in graph:
        for conn in graph[num]:
            recurse(conn, setty)

answers = []
for num in culminate:
    books = set()
    recurse(num, books)
    answers.append(books)

mini = float('inf')
for i in range(len(answers)):
    for j in range(i + 1, len(answers)):
        intersect = answers[i] | answers[j]
        summy = 0
        for book in intersect:
            summy += arr[book - 1]
        mini = min(mini, summy)
        
print(mini)