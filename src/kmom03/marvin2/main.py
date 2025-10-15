"""
Marvin with a simple menu to start up with.
Marvin doesn't do anything, just presents a menu with some choices.
You should add functionally to Marvin.
"""

import marvin1
import marvin2

marvin_image = r"""

 |\/\/\/|
 |      |
 |      |
 | (o)(o)
 C      _)
 | ,___|
 |   /
 /____\
/      \

"""

def show_menu():
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Bart Simpson ¡Ay, caramba! Wassup?")
        print("1) Who are you?")
        print("2) Celsius to Fahrenheit?")
        print("3) Did you pass? What grade?")
        print("4) larger or smaller")
        print("5) Social security number")
        print("6) The Robber Language")
        print("7) Birthdays last four digits")
        print("8) The string randomizer")
        print("q) Quit.")

def handle_choice(choice):
        if choice == "1":
            marvin1.greet()
        elif choice == "2":
            marvin1.celsius_to_fahrenheit()
        elif choice == "3":
            marvin1.points_to_grade()
        elif choice == "4":
            marvin1.compare_numbers()
        elif choice == "5":
            marvin1.validate_ssn()
        elif choice == "6":
            marvin1.robber_language()
        elif choice == "7":
            birthday = input("Enter birthday daye (YYMMDD): ")
            print(marvin2.create_ssn(birthday))
        elif choice == "8":
            text = input("Enter a string to randomize: ")
            print(f"{text} --> {marvin2.randomize_string(text)}")
        else:
            print("That is not a valid choice. You can only choose from the menu.")

def main():
    stop = False
    while not stop:
        show_menu()
        choice = input("Choose thrue number: ")

        if choice == "q":
            print("Bah")
            stop = True
        else:
            handle_choice(choice)
        if not stop:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
