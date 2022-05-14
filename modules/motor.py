# Description: Code for powering DC motor with L293
# Author: C20
# Notes
# - Week 9 Practical
# - Milestone 4 (Fan + Buzzer)

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp
from modules.file    import get_system_parameter
from modules.buzzer  import sound_buzzer

from storage import coldReadings, heatReadings, fastReadings


pin1A = int(get_system_parameter(name="1A"))
pin2A = int(get_system_parameter(name="2A"))

coldTemp = float(get_system_parameter(name="cold"))
roomTemp = float(get_system_parameter(name="room"))
hotTemp  = float(get_system_parameter(name="hot" ))


def motor(board: Pymata4):

    """Runs motor for x seconds depending on the temperature"""

    board.set_pin_mode_pwm_output(pin1A)
    board.set_pin_mode_pwm_output(pin2A)
    print(f"{get_timestamp()} - Motor: ON")

    tempReadings = heatReadings

    for i in range(len(tempReadings)):

        currentTemp  = tempReadings[i]

        if currentTemp > hotTemp:

            state = "Hot (AC On)"
            speed = int(5*currentTemp + 50)

            #turn left for AC
            board.pwm_write(pin1A, 0)
            board.pwm_write(pin2A, speed)

            if currentTemp - tempReadings[i-3] > 1 and i > 3:
                sound_buzzer(board, state="rapid up temp")
            else:
                sound_buzzer(board, state="off")

        elif currentTemp < coldTemp:

            state = "Cold (Heat On)"
            speed = int(-5*currentTemp + 300)

            # turn right for heater
            board.pwm_write(pin1A, speed)
            board.pwm_write(pin2A, 0)

            if tempReadings[i-3] - currentTemp > 1 and i > 3:
                sound_buzzer(board, state="rapid down temp")
            else:
                sound_buzzer(board, state="off")

        else:

            state = "Room (Fan Off)"
            speed = 0
            board.pwm_write(pin1A, 0)
            board.pwm_write(pin2A, 0)

        print(f"{get_timestamp()} - Temp: {currentTemp} \t State: {state} \t Speed: {speed}")

        time.sleep(1)

    board.pwm_write(pin1A, 0)
    board.pwm_write(pin2A, 0)
    print(f"{get_timestamp()} - Motor: OFF")

    return
