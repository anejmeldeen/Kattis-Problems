n, m = list(map(int, input().split()))
notes = []
for _ in range(n):
    notes.append(int(input()))

mappy = {'ppp': 0, 'pp': 1, 'p': 2, 'mp': 3, 'mf': 4, 'f': 5, 'ff': 6, 'fff': 7}

note_sound = []
tuples = []
for _ in range(m):
    data = input().split()
    num = int(data[0])
    sound = mappy[data[1]]
    note_sound.append((num, sound))
idx = 0
for i in range(m):
    note, sound = note_sound[i]
    if i == m - 1:
        while idx < n:
            tuples.append((notes[idx], sound))
            idx += 1
    else:
        next_note, _ = note_sound[i + 1]
        while idx < next_note - 1:
            tuples.append((notes[idx], sound))
            idx += 1

tuples.sort(key=lambda x: (x[0], -x[1]))

counts = {i: 0 for i in range(8)}

violation = 0
for i in range(n):
    note, sound = tuples[i]
    counts[sound] += 1
    for j in range(sound + 1, 8):
        violation += counts[j]

print(violation)