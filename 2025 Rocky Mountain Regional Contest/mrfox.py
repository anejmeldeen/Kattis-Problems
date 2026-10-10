from collections import defaultdict

n, m, l = list(map(int, input().split()))


move_speed = []
for _ in range(n):
    moves = list(map(int, input().split()))
    move_speed.append(moves)

died_made = set()

move_counter = defaultdict(int)
for _ in range(m):
    move = int(input())
    made_it = set()
    if move == 12:
        kill_me_right = float('inf')
        kill_me_left = float('inf')
        for i in range(n):
            if i in died_made:
                continue
            pos = 0
            for time in move_counter:
                pos += time * move_counter[time] * move_speed[i][time - 1]
            if pos >= l:
                made_it.add(i)
            elif pos >= l / 2:
                d = l - pos
                made_it.add(i)
                if l < 4 * d:
                    kill_me_right = min(kill_me_right, i)
            else:
                d = pos
                if l < 4 * d:
                    kill_me_left = min(kill_me_left, i)
            
        move_counter = defaultdict(int)

        if kill_me_right != float('inf'):
            made_it.discard(kill_me_right)
        elif kill_me_left != float('inf'):
            made_it.discard(kill_me_left)
        
        made_it = sorted(made_it)
        for x in made_it:
            died_made.add(x)
        if len(made_it) > 0:
            print(' '.join(list(map(lambda x:str(x + 1), made_it))))
        else:
            print("None")
        if kill_me_right != float('inf'):
            print(kill_me_right + 1)
            died_made.add(kill_me_right)
        elif kill_me_left != float('inf'):
            print(kill_me_left + 1)
            died_made.add(kill_me_left)
        else:
            print("None")
    else:
        move_counter[move] += 1