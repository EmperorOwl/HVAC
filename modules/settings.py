# Description: Code authenticating user and
# Author: C20
# Notes:
# - Block 5 - Security

from modules.console import get_timestamp, italicise_text
from modules.file    import get_system_parameter
from modules.file    import update_system_parameter


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
        correctPin = get_system_parameter(name="PIN")

        if enteredPin == correctPin:
            print(f"{get_timestamp()} - Access Granted: Correct Pin")
            loggedIn = True

        else:
            print(f"{get_timestamp()} - Access Denied: Incorrect Pin")
            failedAttempts += 1

    return loggedIn


def check_system_parameter(name: str, value: str):

    """A function that verifies the new value for a system parameter against logical ranges"""

    passed = False

    if name == "PIN":

        if len(value) == 4:
            try:
                pin = int(value)
                if pin >= 0:
                    passed = True
                else:
                    print(f"{get_timestamp()} - ERROR: Pin must be a positive four-digit number.")
            except ValueError:
                print(f"{get_timestamp()} - ERROR: Pin must be a positive four-digit number.")
        else:
            print(f"{get_timestamp()} - ERROR: Pin must be a positive four-digit number.")

    elif name in ["HOT", "ROOM", "COLD"]:

        try:
            temp = float(value)
            if -20 <= temp <= 40:
                passed = True
            else:
                print(f"{get_timestamp()} - ERROR: Temperature must be in between -20°C and 40°C.")
        except ValueError:
            print(f"{get_timestamp()} - ERROR: Temperature must be a number.")

    elif name in ["D1", "D2", "D3", "D4", "SER", "RCLK", "SRCLK", "TRIGGER", "ECHO"]:
        passed = True

    elif name in ["BUZZER", "1A", "2A"]:
        pwmPins = [3, 5, 6, 9, 10, 11]

        if value in pwmPins:
            passed = True
        else:
            print(f"{get_timestamp()} - ERROR: Arduino pin for {name} must support PWM.")

    else:
        print(f"{get_timestamp()} - ERROR: Parameter {name} does not exist.")

    return passed


def display_settings():

    """A function that controls the settings menu"""

    if authenticate_user() is True:

        while True:

            timestamp = get_timestamp()
            whitespace = " " * (len(timestamp) + 2)

            print()
            print(f"{timestamp} - HVAC Settings")
            print(f"{whitespace} {italicise_text('Instructions: Type the name and new value of the parameter')}")
            print(f"{whitespace} {italicise_text('Examples: pin 1234, hot 30, exit')}")
            print(f"{whitespace} 1. Pin <new pin>")
            print(f"{whitespace} 2. Hot | Room | Cold <new temp>")
            print(f"{whitespace} 3. D1 | D2 | D3 | D4 <new arduino pin>")
            print(f"{whitespace} 4. SER | RCLK | SRCLK <new arduino pin>")
            print(f"{whitespace} 5. Buzzer | 1A | 2A <new arduino pwm pin>")
            print(f"{whitespace} 6. Trigger | Echo <new arduino pin>")
            print(f"{whitespace} 5. Exit or 0")

            parameter = input(f"{get_timestamp()} - HVAC Parameter: ")
            name = parameter.split(" ")[0].upper()

            if name not in ["exit", "0"]:
                value = parameter.split(" ")[1]

                if check_system_parameter(name, value) is True:
                    update_system_parameter(name, value)
                    print(f"{get_timestamp()} - Parameter {name} has been updated to {value}.")

            else:
                break

    return
