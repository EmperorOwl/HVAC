# Description: Code for buzzer
# Author: C20
# Notes
# - Milestone 4 (Fan + Buzzer)
# - Squiggly line on top of Arduino pins means that it can be used as PWM output

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp

buzzerPin = 9

def sound_buzzer(board: Pymata4, state: str):

    board.set_pin_mode_pwm_output(buzzerPin)

    if state.lower() == "rapid up temp":

        print(f"{get_timestamp()} - Rapid Up Temp: High Buzzer Sound Activated")
        board.pwm_write(buzzerPin, 20)
        time.sleep(0.5)
        board.pwm_write(buzzerPin, 0)

    elif state.lower() == "rapid down temp":

        print(f"{get_timestamp()} - Rapid Down Temp: Low Buzzer Sound Activated")
        board.pwm_write(buzzerPin, 3)
        time.sleep(0.5)
        board.pwm_write(buzzerPin, 0)

    else:
        board.pwm_write(buzzerPin, 0)

    return
