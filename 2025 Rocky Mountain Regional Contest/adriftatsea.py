curr = input()
need = input()

degree = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}

if curr == need:
    print("Keep going straight")
elif (degree[need] - degree[curr]) % 360 == 180:
    print("U-turn")
else:
    diff = (degree[curr] - degree[need]) % 360
    word = "port"
    if diff > 180:
        word = "starboard"
    if word == "starboard":
        diff = 360 - diff
    print(f"Turn {diff % 180} degrees {word}")