n = int(input())

game_map = {"fishing": "alice", "golf": "bob", "hockey": "charlie"}

for _ in range(n):
    request = input().split()
    name = request[0]
    game = request[-1]

    if game_map[game] == name:
        print(f"{name} already has {game}")
    else:
        print(f"{name} borrows {game} from {game_map[game]}")
        game_map[game] = name