from pymata4 import pymata4

from modules.console import get_timestamp, display_menu, display_settings

while True:

    try:
        board = pymata4.Pymata4()
        print(f"{get_timestamp()} - HVAC System is online!")
        break

    except RuntimeError:
        pass


while True:

    display_menu()

    function = input(f"{get_timestamp()} - HVAC Function: ")
    choice = function.split(" ")[0].lower()

    try:

        if choice == "blink":
            from modules.electrical import blink
            blink(board)

        elif choice == "light":
            from modules.electrical import light
            light(board, buttonPin=0, lightPin=1)

        elif choice == "display":
            from modules.shift import display
            display(board, string=function.split(" ")[1])

        elif choice == "timer":
            from modules.shift import timer
            timer(board, x=int(function.split(" ")[1]))

        elif choice == "sonar":
            from modules.ultra import run_sonar
            run_sonar(board, triggerPin=2, echoPin=3, x=int(function.split(" ")[1]))

        elif choice == "settings":
            display_settings()

        elif choice == "quit" or choice == "0":
            print(f"{get_timestamp()} - HVAC System is offline!")
            board.shutdown()
            quit()

        else:
            print(f"{get_timestamp()} - Incorrect function selected")

    except KeyboardInterrupt:
            print(f"{get_timestamp()} - Current process interrupted")
