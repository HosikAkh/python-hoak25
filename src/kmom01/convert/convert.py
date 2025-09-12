x = input("Enter value to convert: ")

if x.isdigit():
    value = float(x)

    choice = ("""
    P: Price, before --> after discount and tax
    S: Speed, km/h --> mph
    """)
    y = input(f"Choose what to convert: {choice} \n:")
    select = y.lower()

    if select in {"p", "price"}:
        discount = value - 10
        final_price = discount * 1.2
        print(f"{value:.1f} before discount, {final_price} after the discount and tax")
    elif select in {"s", "speed"}:
        converted_value = round(value * 0.62137, 2)
        print(f"{value:.1f} km/h is {converted_value} mph")
    else:
        print("Invalid converter, please enter P or S.")
        exit()
else:
    print("Invalid value, please enter a number.")
    exit()
