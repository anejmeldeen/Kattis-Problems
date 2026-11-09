import random
res = []
choices = ["T", "F"]

res = ["1000"]
for _ in range(1000):
    res.append("10")
    res.append("FTFTFTFTFT")
res = '\n'.join(res)

print(res)

filey = open("South Division/1.in", "w")
filey.write(res)