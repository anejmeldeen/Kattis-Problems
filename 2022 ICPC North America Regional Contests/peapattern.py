n, m = input().split()

def get_next(numby):
    digit_count = {}
    for char in numby:
        digit_count[char] = digit_count.get(char, 0) + 1

    number_str = "0123456789"
    new_str = ""
    for num in number_str:
        if num not in digit_count:
            continue
        new_str += str(digit_count[num]) + num
    
    return new_str

found = False
count = 1
for i in range(101):
    if n == m:
        found = True
        break
    n = get_next(n)
    count += 1

if found:
    print(count)
else:
    print("Does not appear")