# Description: Code for authenticating user to settings menu
# Author: C20
# Notes:
# - Block 5 - Security

import time

from modules.console import get_timestamp, italicise_text
from modules.file    import get_system_parameter


unlockTime = time.time()  # variable for holding the time the user can log in again after three incorrect attempts

def authenticate_user():

    """A function that checks whether the user has entered the correct pin"""

    global unlockTime
    loggedIn = False
    attempts = 1

    if time.time() >= unlockTime:

        while loggedIn is False and attempts <= 3:

            timestamp = get_timestamp()
            whitespace = " " * (len(timestamp) + 2)

            print()
            print(f"{timestamp} - HVAC Security")
            print(f"{whitespace} {italicise_text('Instructions: Type the correct four digit pin')}")
            print(f"{whitespace} {italicise_text(f'Number of Attempts: {attempts}')}")

            enteredPin = input(f"{get_timestamp()} - HVAC Pin: ")
            correctPin = get_system_parameter(name="PIN")

            if enteredPin == correctPin:
                print(f"{get_timestamp()} - Access Granted: Correct Pin")
                loggedIn = True

            elif attempts == 3:
                print(f"{get_timestamp()} - Access Denied: Three Incorrect Attempts (Two Minutes Timeout Activated)")
                unlockTime = time.time() + 2*60
                attempts += 1

            else:
                print(f"{get_timestamp()} - Access Denied: Incorrect Pin")
                attempts += 1

    else:
        print(f"{get_timestamp()} - Access Denied: Three Previous Incorrect Attempts")
        print(f"{get_timestamp()} - Two Minutes Timeout: {round(unlockTime - time.time(), 2)} s left")

    return loggedIn
