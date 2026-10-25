import sys

n = int(input())

potential = [i for i in range(1, n + 1)]
while len(potential) > 1:
    new = []
    for i in range(0, len(potential), 2):
        if i + 1 < len(potential):
            a = potential[i]
            b = potential[i + 1]
            print(f"? {a} {b}")
            sys.stdout.flush()

            val = int(input())
            if val == 0:
                new.append(a)
            else:
                new.append(b)
        else:
            new.append(potential[i])
    potential = new

# we are done, assuming the king always exists
print(f"! {potential[0]}")