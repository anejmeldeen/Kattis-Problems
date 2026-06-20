k, r = list(map(int, input().split()))
stock = list(map(int, input().split()))

recipes = []
for _ in range(r):
    data = list(map(int, input().split()))
    recipe = data[:-1]
    price = data[-1]

    recipes.append((recipe, price))

best = 0
for recipe, price in recipes:
    amt = float('inf')
    for i, ingredient in enumerate(recipe):
        if ingredient == 0:
            continue
        amt = min(amt, stock[i] // ingredient)
    best = max(best, amt * price)

print(best)