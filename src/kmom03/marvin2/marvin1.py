def greet ():
    name = input("What is your name? ")
    print("\nBart Simpson says:\n")
    print(f"Wassup {name} - Eat my shorts!")
    print("What can I do you for?!")

def celsius_to_fahrenheit():
    try:
        celsius = float(input("Wanna see magic? Say any temperature in Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    except ValueError:
        print("Say numbers!")

def points_to_grade():
    try:
        max_points = float(input("The maximum of points: "))
        your_points = float(input("Yours: "))

        if your_points >= 0.9 * max_points:
            grade = "A"
        elif your_points >= 0.8 * max_points:
            grade = "B"
        elif your_points >= 0.7 * max_points:
            grade = "C"
        elif your_points >= 0.6 * max_points:
            grade = "D"
        elif your_points >= 0.5 * max_points:
            grade = "E"
        elif your_points < 0.5 * max_points:
            grade = "F"
        
        print(f"score: {grade}")

    except:
                print("Numbers!!")

def compare_numbers():
    storage = None
    while True:
        user_input = input("Enter number (or 'done' to exit): ")

        if user_input.lower() == "done":
            break

        try:
            number = float(user_input)
            if storage is None:
                next_input = input("Enter another number to compare: ")
                try:
                    next_number = float(next_input)
                    if next_number > number:
                        print("larger!")
                    elif next_number < number:
                        print("smaller!")
                    else:
                        print("same!")
                    storage = next_number
                except ValueError:
                    print("not a number!")
                    storage = number
                else:
                    if number > storage:
                        print("larger!")
                    elif number < storage:
                        print("smaller!")
                    else:
                        print("same!")
                    storage = number
        except ValueError:
            print("not a number!")

def validation_of_ssn():
    On = True
    while On:
        enter = input("Enter social number(YYMMDD-XXXZ or YYMMDDXXXX): ")

        Security_code = ""
        Wrong_numb = False

        for numb in enter:
            if numb.isdigit():
                Security_code += numb
            elif numb == "-":
                pass
            else:
                Wrong_numb = True
                break
        
        if Wrong_numb or len(Security_code) != 10:
            print("Not valid")
        else:
            total = 0
            for i in range(10):
                v = int(Security_code[i])
                if i % 2 == 0:
                    v = v * 2
                    if v > 9:
                        v = v // 10 + v % 10
                total += v

            if total % 10 == 0:
                print("Valid")
            else:
                print("Not valid")
        break

def robber_language():
    vocals = "aeiouyåäöAEIOUYÅÄÖ"
    words = input("Write one word: ")
    transfer = ""

    for i in words:
        if i.isalpha() and i not in vocals:
            transfer +=  i + "o" + i.lower()
        else:
            transfer += i
    
    print(transfer)
