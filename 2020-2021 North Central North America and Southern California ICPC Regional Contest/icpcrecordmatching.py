import sys
data = sys.stdin.readlines()

a = []
b = []
first_done = False

for record in data:
    if record == "\n":
        first_done = True
        continue

    first, last, email = record.split()
    if not first_done:
        a.append((first, last, email))
    else:
        b.append((first, last, email))

a_found = set()
b_found = set()
for i, datab in enumerate(b):
    for j, dataa in enumerate(a):
        bfirst, blast, bemail = datab
        afirst, alast, aemail = dataa
        bfirst = bfirst.lower()
        blast = blast.lower()
        bemail = bemail.lower()
        afirst = afirst.lower()
        alast = alast.lower()
        aemail = aemail.lower()
        if afirst == bfirst and alast == blast:
            a_found.add(j)
            b_found.add(i)
        if aemail == bemail:
            a_found.add(j)
            b_found.add(i)

sol1 = []
for i, a_record in enumerate(a):
    first, last, email = a_record
    if i in a_found:
        continue
    sol1.append(((email.lower(), last.lower(), first.lower()), f"I {email} {last} {first}"))
sol2 = []
for i, b_record in enumerate(b):
    first, last, email = b_record
    if i in b_found:
        continue
    sol2.append(((email.lower(), last.lower(), first.lower()), f"O {email} {last} {first}"))

sol = sorted(sol1) + sorted(sol2)

if len(sol) == 0:
    print("No mismatches.")
else:
    for row in sol:
        print(row[1])