# Week 3 & 4 Practical
# - Blink
# - Light

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp


def blink(board: Pymata4, outputPin: int = 13, x: int = 4):

    """A function to toggle a digital pin x times."""

    board.set_pin_mode_digital_output(outputPin)

    for i in range(x):

        print(f"{get_timestamp()} - Pin {outputPin}: ON")
        board.digital_write(outputPin, 1)
        time.sleep(1)

        print(f"{get_timestamp()} - Pin {outputPin}: OFF")
        board.digital_write(outputPin, 0)
        time.sleep(1)

    return


def light(board: Pymata4, buttonPin: int, lightPin: int, x: float = 5):

    """A function to monitor for x minutes whether a button is pressed to turn on LED."""

    board.set_pin_mode_digital_input(buttonPin)
    board.set_pin_mode_digital_output(lightPin)

    endTime = time.time() + x * 60

    lightState = 0

    while time.time() < endTime:

        time.sleep(1)

        currentState, timeStamp = board.digital_read(buttonPin)

        if currentState == 0:

            if lightState == 0:
                lightState = 1
                print(f"{get_timestamp()} - Button has been pressed. LED has been switched on.")

            else:
                lightState = 0
                print(f"{get_timestamp()} - Button has been pressed. LED has been switched off.")

        board.digital_write(lightPin, lightState)

    board.digital_write(lightPin, 0)
    print(f"{get_timestamp()} - HVAC has stopped monitoring button state as it has been {x} minutes. "
          f"LED has been switched off.")

    return
