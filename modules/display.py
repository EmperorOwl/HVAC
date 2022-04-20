# Week 5 Practical
# - Seven segment display without shift register
# - Takes up 11 pins on the Arduino

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp


def setup(board: Pymata4):

    # top of display
    dig1 = 2
    segA = 3
    segF = 4
    dig2 = 5
    dig3 = 6
    segB = 7

    # bottom of display
    segE = 8
    segD = 9
    deci = 10
    segC = 11
    segG = 12
    dig4 = 13

    digits = [dig1, dig2, dig3, dig4]
    for dig in digits:
        board.set_pin_mode_digital_output(dig)
        board.digital_write(dig, 1)  # disable digits

    segments = [segA, segB, segC, segD, segE, segF, segG]
    for seg in segments:
        board.set_pin_mode_digital_output(seg)

    return digits, segments


def display_character(board: Pymata4, segments: list, char: str, dig: int, turnOff: bool = False):

    from storage import charLookup
    values = charLookup[char]

    for i in range(0, 7):
        board.digital_write(segments[i], int(values[i]))

    board.digital_write(dig, 0)

    if turnOff:
        board.digital_write(dig, 1)

    return


def display(board: Pymata4, string: str, x: float = 1):

    """A function to ask user to display a string for x minutes."""

    digits, segments = setup(board)

    print(f"{get_timestamp()} - Attempting to display {string} for {x} minutes.")

    endTime = time.time() + x * 60
    while time.time() < endTime:

        time.sleep(0.0025)  # prevent laptop from crashing

        for i in range(len(string)):
            char = string[i]
            dig = digits[i]

            try:
                display_character(board, segments, char, dig, turnOff=True)
            except KeyError:
                pass

    for digit in digits:
        board.digital_write(digit, 1)
    print(f"{get_timestamp()} - Seven segment display has been switched off.")

    return


def timer(board: Pymata4, x: int = 9):

    """A function to countdown from x seconds"""

    digits, segments = setup(board)

    for sec in range(x, -1, -1):

        time.sleep(1)
        display_character(board, segments, char=str(sec), dig=digits[0])

        if sec == 0:
            print(f"{get_timestamp()} - Time's up!")

        elif sec == 1:
            print(f"{get_timestamp()} - Timer (1 second left)")

        else:
            print(f"{get_timestamp()} - Timer ({sec} seconds left)")

    time.sleep(5)
    board.digital_write(digits[0], 1)
    print(f"{get_timestamp()} - Seven segment display has been switched off.")

    return
