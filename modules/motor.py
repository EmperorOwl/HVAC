# Description: Code for powering DC motor with L293
# Author: C20
# Notes
# - Week 9 Practical
# - Milestone 4 (Fan + Buzzer)

import time
from pymata4.pymata4 import Pymata4

from modules.console import get_timestamp
from modules.buzzer import sound_buzzer

pin1A = 10
pin2A = 11

coldTemp = 20
roomTemp = 25
hotTemp  = 30


coldTempReadings = [30, 28, 26, 24, 22, 20] + \
                   [19 for i in range(3)] + \
                   [18 for i in range(3)] + \
                   [17 for i in range(3)] + \
                   [16 for i in range(3)] + \
                   [15 for i in range(3)] + \
                   [14 for i in range(3)] + \
                   [13 for i in range(3)] + \
                   [12 for i in range(3)] + \
                   [11 for i in range(3)] + \
                   [10 for i in range(3)]

heatTempReadings = [20, 22, 24, 26, 28, 30] + \
                   [31 for i in range(3)] + \
                   [32 for i in range(3)] + \
                   [33 for i in range(3)] + \
                   [34 for i in range(3)] + \
                   [35 for i in range(3)] + \
                   [36 for i in range(3)] + \
                   [37 for i in range(3)] + \
                   [38 for i in range(3)] + \
                   [39 for i in range(3)] + \
                   [40 for i in range(3)]

fastTempReadings = [31 for i in range(1)] + \
                   [33 for i in range(2)] + \
                   [35 for i in range(3)] + \
                   [37 for i in range(4)] + \
                   [40 for i in range(5)]


def motor(board: Pymata4):

    """Runs motor for x seconds depending on the temperature"""

    board.set_pin_mode_pwm_output(pin1A)
    board.set_pin_mode_pwm_output(pin2A)
    print(f"{get_timestamp()} - Motor: ON")

    tempReadings = heatTempReadings

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
