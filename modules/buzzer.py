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

def setup_buzzer(board: Pymata4):

    """A function to set up buzzer"""

    board.set_pin_mode_pwm_output(buzzerPin)

    return


def sound_buzzer(board: Pymata4, intensity: int, duration: float):

    """A function to sound buzzer"""
    board.pwm_write(buzzerPin, intensity)
    time.sleep(duration)
    board.pwm_write(buzzerPin, 0)

    return


def test_buzzer(board: Pymata4, intensity: int, duration: float):

    """A function to test buzzer"""

    setup_buzzer(board)
    print(f"{get_timestamp()} - Buzzer: ON")
    print(f"{get_timestamp()} - Intensity: {intensity}/255 \t Duration: {duration} s")
    sound_buzzer(board, intensity, duration)
    print(f"{get_timestamp()} - Buzzer: OFF")

    return
