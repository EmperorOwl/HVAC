# Description: Code for seven-segment display with shift register
# Author: C20
# Notes:
# - Week 7 Practical
# - Four digital pins used to control the four common digits
# - Three digital pins for SER, RCLK and SRCLK

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp
from modules.file    import get_system_parameter


def setup_display(board: Pymata4):

    """A function that prepares all pins for use in the seven segment display"""

    # Digit 1 (D1) common pin which when set to HIGH activates the first digit
    dig1 = int(get_system_parameter(name="DIG1"))
    # Digit 2 (D2) common pin which when set to HIGH activates the second digit
    dig2 = int(get_system_parameter(name="DIG2"))
    # Digit 3 (D3) common pin which when set to HIGH activates the third digit
    dig3 = int(get_system_parameter(name="DIG3"))
    # Digit 4 (D4) common pin which when set to HIGH activates the fourth digit
    dig4 = int(get_system_parameter(name="DIG4"))

    # Serial input pin (SER) used to feed data into the shift register a bit at a time
    dataPin = int(get_system_parameter(name="SER"))
    # Register latch (RCLK) which when set to HIGH stores the contents of the shift register
    latchPin = int(get_system_parameter(name="RCLK"))
    # Shift register clock (SRCLK) which when set to HIGH will shift bits into the shift register
    clockPin = int(get_system_parameter(name="SRCLK"))

    digits = [dig1, dig2, dig3, dig4]
    for dig in digits:
        board.set_pin_mode_digital_output(dig)
        board.digital_write(dig, 1)  # turn off all digits due to negative logic

    pins = [dataPin, latchPin, clockPin]
    for pin in pins:
        board.set_pin_mode_digital_output(pin)

    return digits, pins


def check_string(string: str):

    """A function that checks each character in the string before outputting to the seven segment display"""

    for i in range(len(string)):

        char = string[i]

        if char in ['B', 'D', 'N', 'Q', 'R', 'T', 'Y']:
            string = string[:i] + char.lower() + string[i+1:]
            print(f"{get_timestamp()} - The letter {char} cannot be displayed. "
                  f"Its lowercase equivalent will instead be used.")

        elif char in ['e', 'f', 'g', 'i', 'j', 'l', 'p', 's']:
            string = string[:i] + char.upper() + string[i+1:]
            print(f"{get_timestamp()} - The letter {char} cannot be displayed. "
                  f"Its uppercase equivalent will instead be used.")

        elif char in ['k', 'm', 'v', 'w', 'x', 'z']:
            print(f"{get_timestamp()} - The letter {char} cannot be displayed. "
                  f"It will be skipped.")

    return string


def display_character(board: Pymata4, pins: list, char: str, digit: int, turnOff: bool = False):

    """A function that outputs a single character to the seven segment display"""

    dataPin, latchPin, clockPin = pins[0], pins[1], pins[2]

    from storage import charLookup
    values = charLookup[char]  # fetch character encoding, i.e. the segment values
    values = '0' + values  # add zero due to decimal point being first output pin
    values = values[::-1]  # reverse sequence due to nature of shift register

    board.digital_write(latchPin, 0)  # turn off latch

    for value in values:

        board.digital_write(dataPin, int(value))  # send one bit and shift previous bits down
        board.digital_write(clockPin, 1)  # turn on clock
        board.digital_write(clockPin, 0)  # turn off clock

    board.digital_write(latchPin, 1)  # turn on latch

    board.digital_write(digit, 0)  # turn on digit

    if turnOff:
        time.sleep(0.0025)
        board.digital_write(digit, 1)

    return


def test_display(board: Pymata4, string: str, x: int):

    """A function display user's specified string for x seconds."""

    digits, pins = setup_display(board)
    print(f"{get_timestamp()} - Seven segment display: ON")

    string = check_string(string)
    print(f"{get_timestamp()} - Displaying {string} for {x} seconds ...")

    endTime = time.time() + 0.55*x
    while time.time() < endTime:

        for i in range(len(string)):

            char = string[i]
            dig = digits[i]

            try:
                display_character(board, pins, char, dig, turnOff=True)
            except KeyError:
                pass

    time.sleep(0.45*x)
    for digit in digits:
        board.digital_write(digit, 1)
    print(f"{get_timestamp()} - Seven segment display: OFF")

    return


def display(board: Pymata4, digits: list, pins: list, string: str):

    """
    A function to display for integration purposes
    - Must call setup_display before
    - No stuff printed
    - Will not check string for illegal characters
    - Only displays for one second
    """
    for _ in range(20):
        for i in range(len(string)):

            char = string[i]
            dig = digits[i]

            display_character(board, pins, char, dig, turnOff=True)

    return


def timer(board: Pymata4, x: int):

    """A function to countdown from x seconds"""

    digits, pins = setup_display(board)
    print(f"{get_timestamp()} - Seven segment display: ON")

    for sec in range(x, -1, -1):

        time.sleep(1)
        display_character(board, pins, char=str(sec), digit=digits[0])

        if sec == 0:
            print(f"{get_timestamp()} - Time's up!")

        else:
            print(f"{get_timestamp()} - Timer: {sec} s")

    time.sleep(5)
    board.digital_write(digits[0], 1)
    print(f"{get_timestamp()} - Seven segment display: OFF")

    return
