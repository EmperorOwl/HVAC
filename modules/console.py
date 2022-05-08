# Description: Code for asking inputs and displaying outputs
# Author: C20
# Notes:
# - Week 5 Practical
# - Menu logic
# - Milestone 5 Systems Parameters + Security

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


def update_fan(newSpeed: str):

    """A function that updates the fan speed"""

    lowerBound = 0
    upperBound = 100

    try:
        spd = int(newSpeed)

        if lowerBound < spd < upperBound:
            print(f"{get_timestamp()} - Fan speed has been updated to {newSpeed}")

        else:
            print(f"{get_timestamp()} - Fan speed must be in between {lowerBound} and {upperBound}")

    except ValueError:
        print(f"{get_timestamp()} - Fan speed must be a positive number.")

    return


def update_pin(newPin: str):

    """A function that updates the pin to modify any system parameters"""

    if len(newPin) == 4:

        try:
            pin = int(newPin)

            if pin >= 0:
                print(f"{get_timestamp()} - Pin has been updated to {newPin}")

            else:
                print(f"{get_timestamp()} - Pin must be a positive four-digit number.")

        except ValueError:
            print(f"{get_timestamp()} - Pin must be a positive four-digit number.")

    else:
        print(f"{get_timestamp()} - Pin must be a positive four-digit number.")

    return


def get_pin():

    """A function that retrieves the correct pin from a text file"""

    file = open('parameters.txt', 'r')
    parameters = file.readlines()

    for parameter in parameters:
        if parameter.startswith("authenticationPin"):
            correctPin = parameter.split(" = ")[1].strip('\n')

    return correctPin


def authenticate_user():

    """A function that checks whether the user has entered the correct pin"""

    loggedIn = False
    failedAttempts = 0

    while loggedIn is False and failedAttempts <= 5:

        timestamp = get_timestamp()
        whitespace = " " * (len(timestamp) + 2)

        print()
        print(f"{timestamp} - HVAC Security")
        print(f"{whitespace} {italicise_text('Instructions: Type the correct four digit pin')}")
        print(f"{whitespace} {italicise_text(f'Number of Failed Attempts: {failedAttempts}')}")

        enteredPin = input(f"{get_timestamp()} - HVAC Pin: ")
        correctPin = get_pin()

        if enteredPin == correctPin:
            print(f"{get_timestamp()} - Access Granted: Correct Pin")
            loggedIn = True

        else:
            print(f"{get_timestamp()} - Access Denied: Incorrect Pin")
            failedAttempts += 1

    return loggedIn


def display_menu():

    """A function that displays the actions the user can do"""

    timestamp = get_timestamp()
    whitespace = " " * (len(timestamp) + 2)

    print()
    print(f"{timestamp} - HVAC Menu")
    print(f"{whitespace} {italicise_text('Instructions: Type the name and arguments of the function')}")
    print(f"{whitespace} {italicise_text('Examples: display 1234 5, timer 9, quit')}")
    print(f"{whitespace} 1. Blink")
    print(f"{whitespace} 2. Light")
    print(f"{whitespace} 3. Display <string> <seconds>")
    print(f"{whitespace} 4. Sonar <seconds>")
    print(f"{whitespace} 5. Timer <seconds>")
    print(f"{whitespace} 6. Settings")
    print(f"{whitespace} 7. Quit or 0")

    return


def display_settings():

    """A function that controls the settings menu"""

    if authenticate_user() is True:

        timestamp = get_timestamp()
        whitespace = " " * (len(timestamp) + 2)

        print()
        print(f"{timestamp} - HVAC Settings")
        print(f"{whitespace} {italicise_text('Instructions: Type the name and new value of the parameter')}")
        print(f"{whitespace} {italicise_text('Examples: fan 21, pin 1234, exit')}")
        print(f"{whitespace} 1. Fan <new speed>")
        print(f"{whitespace} 2. Pin <new pin>")
        print(f"{whitespace} 3. Exit or 0")

        parameter = input(f"{get_timestamp()} - HVAC Parameter: ")
        name = parameter.split(" ")[0].lower()

        if name not in ["exit", "0"]:
            value = parameter.split(" ")[1]

            if name == "fan":
                update_fan(newSpeed=value)

            elif name == "pin":
                update_pin(newPin=value)

            else:
                print(f"{get_timestamp()} - Incorrect parameter selected")

    return
