# Description: Code for reset pin
# Author: C20
# Notes

from pymata4.pymata4 import Pymata4

from modules.file import get_system_parameter


resetPin = int(get_system_parameter(name="RESET"))

def setup_reset(board: Pymata4):

    """A function to set up reset pin"""

    board.set_pin_mode_analog_input(resetPin)

    return


def check_reset(board: Pymata4):

    """A function to check if reset needed"""

    reading = board.analog_read(resetPin)[0]
    if reading < 250:
        reset = True
    else:
        reset = False

    return reset
