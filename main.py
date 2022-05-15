# Description: Main file used to connect to Arduino and run main menu
# Author: C20

from pymata4 import pymata4

from modules.console import get_timestamp
from modules.console import display_menu


while True:

    """
    A loop to keep attempting to connect to the Arduino until a connection is found.
    
    The try-except checks for a RunTimeError which is the error that Python throws when it cannot find the board.
    """

    try:
        board = pymata4.Pymata4()
        print(f"{get_timestamp()} - HVAC System is online!")
        break

    except RuntimeError:
        print(f"{get_timestamp()} - ERROR: Board not found, trying to connect again ...")


while True:

    """
    A loop to control the menu system.
        
    The first try-except checks for a keyboard interrupt which stops the current process.
    The second try-except checks that the user has entered the required arguments to perform the action.
    The conditionals check which action the user has entered and then performs that action.
    The use of split() is to fetch the name and arguments of the action entered.
    
    For example, "display 1234 5", where:
    - "display" is the function name,
    - "1234" is the first argument which tells HVAC the string to show on the seven-segment display and
    - "5" is the second argument which tells HVAC how long to display for in seconds.
    """

    display_menu()

    function = input(f"{get_timestamp()} - HVAC Function: ")
    choice = function.split(" ")[0].lower()

    try:

        try:

            if choice == "blink":
                from modules.electrical import blink
                pin = int(function.split(" ")[1])
                times = int(function.split(" ")[2])
                blink(board, pin, x=times)

            elif choice == "display":
                from modules.shift import display
                string = function.split(" ")[1]
                seconds = int(function.split(" ")[2])
                display(board, string, seconds)

            elif choice == "timer":
                from modules.shift import timer
                seconds = int(function.split(" ")[1])
                timer(board, seconds)

            elif choice == "sonar":
                from modules.ultra import run_sonar
                seconds = int(function.split(" ")[1])
                run_sonar(board, x=seconds)

            elif choice == "motor":
                from modules.motor import motor
                motor(board)

            elif choice == "settings":
                from modules.settings import display_settings
                display_settings()

            elif choice == "quit" or choice == "0":
                print(f"{get_timestamp()} - HVAC System is offline!")
                board.shutdown()
                quit()

            else:
                print(f"{get_timestamp()} - ERROR: Invalid function")

        except IndexError:
            print(f"{get_timestamp()} - ERROR: Missing argument(s)")

    except KeyboardInterrupt:
            print(f"{get_timestamp()} - Current process interrupted")
