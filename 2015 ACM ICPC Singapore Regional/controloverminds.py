n = int(input())
recipes = []
for _ in range(n):
    arr = list(map(int, input().split()))[1:]
    recipes.append(arr)

used = set()
item_to_cauldron = {}
cauldron_to_size = {}
curr_caul = 0
count = 0

for recipe in recipes:
    lengthy = 0
    cauldrons = set()
    for item in recipe:
        if item in used:
            cauldrons.add(item_to_cauldron[item])
        else:
            lengthy += 1

    for caul in cauldrons:
        lengthy += cauldron_to_size[caul]
    
    if lengthy == len(recipe):
        for item in recipe:
            item_to_cauldron[item] = curr_caul
            used.add(item)
        cauldron_to_size[curr_caul] = lengthy
        curr_caul += 1
        count += 1

print(count)