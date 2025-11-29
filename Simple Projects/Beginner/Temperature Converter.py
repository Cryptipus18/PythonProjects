def c_to_f(x):
    f = (x * 9/5) + 32
    return f

def f_to_c(x):
    c = (x - 32) * 5/9
    return c
print("Simple Temperature Converter")
is_looping = True
while is_looping:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    try:
        choice = input("> ")
        if choice.lower() in ("3", "q", "exit"):
            print("Thank you!")
            break
        choice = int(choice)
    except ValueError:
        print("Invalid choice. Enter 1, 2 or 3.")
        continue

    if choice == 1:
        try:
            x = float(input("Temperature in °C: "))
        except ValueError:
            print("Invalid temperature. Try again.")
            continue
        print(f"{c_to_f(x):.2f}°F")
    elif choice == 2:
        try:
            x = float(input("Temperature in °F: "))
        except ValueError:
            print("Invalid temperature. Try again.")
            continue
        print(f"{f_to_c(x):.4f}°C")
    elif choice == 3:
        print("Thank you!")
        break
    else:
        print("Invalid Input. Try again")
