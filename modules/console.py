# Description: Code for asking inputs and displaying outputs
# Author: C20
# Notes:
# - Week 5 Practical
# - Menu logic

import time


def get_timestamp():

    """A function that returns the current time in the form HH:MM:SS as a string"""

    timestamp = time.strftime("%H:%M:%S", time.localtime())

    return timestamp


def ask_user(question):

    """A function that asks a yes/no question to the user and returns their answer"""

    response = False
    while True:

        answer = input(f"{get_timestamp()} - {question}: ").lower()

        if answer == "y":
            response = True
            break

        elif answer == "n":
            break

        else:
            print(f"{get_timestamp()} - Incorrect option selected.")

    return response


def italicise_text(text: str):

    """A function that italicises text for display on the console"""

    italics = "\x1B[3m" + text + "\x1B[0m"

    return italics


def display_menu():

    """A function that displays the actions the user can do"""

    timestamp = get_timestamp()
    whitespace = " " * (len(timestamp) + 2)

    print()
    print(f"{timestamp} - HVAC Menu")
    print(f"{whitespace} {italicise_text('Instructions: Type the name and arguments of the function')}")
    print(f"{whitespace} {italicise_text('Examples: display 1234 5, timer 9, quit')}")
    print(f"{whitespace} 1. Blink <pin> <times>")
    print(f"{whitespace} 3. Display <string> <seconds>")
    print(f"{whitespace} 4. Sonar <seconds>")
    print(f"{whitespace} 5. Timer <seconds>")
    print(f"{whitespace} 6. Motor")
    print(f"{whitespace} 7. Settings")
    print(f"{whitespace} 8. Quit or 0")

    return
