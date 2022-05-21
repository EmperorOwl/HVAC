# Description: Code for updating system parameters
# Author: C20
# Notes:
# - Block 5 - Security

import time

from modules.console  import get_timestamp, italicise_text
from modules.security import authenticate_user
from modules.file     import update_system_parameter


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

    elif name == "DANGER":

        try:
            pin = int(value)
            if 15 <= pin <= 30:
                passed = True
            else:
                print(f"{get_timestamp()} - ERROR: Danger distance must be in between 15 cm and 30 cm.")
        except ValueError:
            print(f"{get_timestamp()} - ERROR: Distance must be a positive number.")

    elif name in ["HOT", "ROOM", "COLD"]:

        try:
            temp = float(value)
            if -20 <= temp <= 40:
                passed = True
            else:
                print(f"{get_timestamp()} - ERROR: Temperature must be in between -20°C and 40°C.")
        except ValueError:
            print(f"{get_timestamp()} - ERROR: Temperature must be a number.")

    elif name in ["D1", "D2", "D3", "D4", "SER", "RCLK", "SRCLK", "TRIGGER", "ECHO", "THERMISTOR", "BUTTON"]:
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

        endTime = time.time() + 2*60  # variable for holding the time when the settings menu should time out

        while True:

            timestamp = get_timestamp()
            whitespace = " " * (len(timestamp) + 2)

            print()
            print(f"{timestamp} - HVAC Settings")
            print(f"{whitespace} {italicise_text('Instructions: Type the name and new value of the parameter')}")
            print(f"{whitespace} {italicise_text('Examples: pin 1234, hot 30, exit')}")
            print(f"{whitespace} 1. Pin <new pin>")
            print(f"{whitespace} 2. Hot | Room | Cold <new temp>")
            print(f"{whitespace} 3. Danger <new distance>")
            print(f"{whitespace} 4. D1 | D2 | D3 | D4 <new arduino pin>")
            print(f"{whitespace} 5. SER | RCLK | SRCLK <new arduino pin>")
            print(f"{whitespace} 6. Buzzer | 1A | 2A <new arduino pwm pin>")
            print(f"{whitespace} 7. Trigger | Echo <new arduino pin>")
            print(f"{whitespace} 8. Thermistor <new analog arduino pin>")
            print(f"{whitespace} 9. Exit or 0")

            parameter = input(f"{get_timestamp()} - HVAC Parameter: ")
            name = parameter.split(" ")[0].upper()

            if time.time() < endTime:

                if name not in ["exit", "0"]:

                    try:
                        value = parameter.split(" ")[1]

                        if check_system_parameter(name, value) is True:
                            update_system_parameter(name, value)
                            print(f"{get_timestamp()} - Parameter {name} has been updated to {value}.")

                    except IndexError:
                        print(f"{get_timestamp()} - ERROR: Missing argument.")

                else:
                    break

            else:
                print(f"{get_timestamp()} - Admin control access has timed out. Please log in again.")
                break

    return
