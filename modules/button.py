# Description: Code for button
# Author: C20
# Notes
# - Button is debounced as the user must hold down for ~0.5 s to count as a press

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp
from modules.file    import get_system_parameter

buttonPin = int(get_system_parameter(name="BUTTON"))

def setup_button(board: Pymata4):

    """A function to set up button"""

    board.set_pin_mode_analog_input(buttonPin)

    return


def check_press(board: Pymata4):

    """A function to check whether button has been pressed"""

    reading = board.analog_read(buttonPin)[0]
    if reading  < 250:
        press = True
    else:
        press = False

    return press


def test_button(board: Pymata4):

    """A function to test button press"""

    setup_button(board)
    print(f"{get_timestamp()} - Button: ON")

    while True:
        time.sleep(1)
        check_press(board)

    return
