# Description: Main file used to connect to Arduino and run main menu
# Author: C20

from pymata4 import pymata4

from modules.console import get_timestamp, display_menu, display_settings


# CONNECT TO ARDUINO
while True:

    try:
        board = pymata4.Pymata4()
        print(f"{get_timestamp()} - HVAC System is online!")
        break

    except RuntimeError:
        pass


# DISPLAY MAIN MENU
while True:

    display_menu()

    function = input(f"{get_timestamp()} - HVAC Function: ")
    choice = function.split(" ")[0].lower()

    try:

        try:

            if choice == "blink":
                from modules.electrical import blink
                blink(board)

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
                run_sonar(board, triggerPin=2, echoPin=3, x=seconds)

            elif choice == "motor":
                from modules.motor import motor
                motor(board)

            elif choice == "settings":
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
