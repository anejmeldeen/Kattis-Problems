x_str = input()
y_str = input()
float_x = float(x_str)
float_y = float(y_str)

x_is_larger = float_x > float_y

x_data = x_str.split(".")
y_data = y_str.split(".")

int_x = int(x_data[0])
int_y = int(y_data[0])
dec_x = int(x_data[1])
dec_y = int(y_data[1])

if int_x > int_y:
    print(x_str)
elif int_y > int_x:
    print(y_str)
else:
    if x_is_larger:
        if dec_x > dec_y:
            print(x_str)
        else:
            print(-1)
    else:
        if dec_y > dec_x:
            print(y_str)
        else:
            print(-1)