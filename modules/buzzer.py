# Description: Code for buzzer
# Author: C20
# Notes
# - Milestone 4 (Fan + Buzzer)
# - Squiggly line on top of Arduino pins means that it can be used as PWM output
# - PWM is a number between 0 - 255

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp
from modules.file    import get_system_parameter

buzzerPin = int(get_system_parameter(name="BUZZER"))

def sound_buzzer(board: Pymata4, state: str):

    """A function to sound the buzzer depending on the temperature state"""

    board.set_pin_mode_pwm_output(buzzerPin)

    if state.lower() == "rapid up temp":

        print(f"{get_timestamp()} - Rapid Up Temp: High Buzzer Sound Activated")

        # send long loud tone
        board.pwm_write(buzzerPin, 50)
        time.sleep(1.5)
        board.pwm_write(buzzerPin, 0)

    elif state.lower() == "rapid down temp":

        print(f"{get_timestamp()} - Rapid Down Temp: Low Buzzer Sound Activated")

        # send short quiet tone
        board.pwm_write(buzzerPin, 5)
        time.sleep(0.5)
        board.pwm_write(buzzerPin, 0)

    else:
        board.pwm_write(buzzerPin, 0)

    return
