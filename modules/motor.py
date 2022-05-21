# Description: Code for powering DC motor with L293
# Author: C20
# Notes
# - Week 9 Practical
# - Milestone 4 (Fan + Buzzer)

import time
from pymata4.pymata4 import Pymata4

from modules.console    import get_timestamp
from modules.file       import get_system_parameter


from storage import coldReadings, heatReadings, fastReadings


pin1A = int(get_system_parameter(name="1A"))
pin2A = int(get_system_parameter(name="2A"))

coldTemp = float(get_system_parameter(name="COLD"))
roomTemp = float(get_system_parameter(name="ROOM"))
hotTemp  = float(get_system_parameter(name="HOT" ))


def setup_motor(board: Pymata4):

    """A function to set up motor"""

    board.set_pin_mode_pwm_output(pin1A)
    board.set_pin_mode_pwm_output(pin2A)

    return


def shutdown_motor(board: Pymata4):

    """A function to shut down motor"""

    board.pwm_write(pin1A, 0)
    board.pwm_write(pin2A, 0)

    return


def run_motor(board: Pymata4, currentTemp: float):

    """A function to run motor depending on current temperature"""

    if currentTemp > hotTemp:

        state = "Hot (AC On)"
        speed = int(5 * currentTemp + 50)

        # turn left for AC
        board.pwm_write(pin1A, 0)
        board.pwm_write(pin2A, speed)

    elif currentTemp < coldTemp:

        state = "Cold (Heat On)"
        speed = int(-5 * currentTemp + 300)

        # turn right for heater
        board.pwm_write(pin1A, speed)
        board.pwm_write(pin2A, 0)

    else:

        state = "Room (Fan Off)"
        speed = 0
        board.pwm_write(pin1A, 0)
        board.pwm_write(pin2A, 0)

    temp = round(currentTemp, 2)
    print(f"{get_timestamp()} - Temp: {temp} \t State: {state} \t Speed: {speed}")

    return


def test_motor(board: Pymata4):

    """A function to test motor"""

    setup_motor(board)
    print(f"{get_timestamp()} - Motor: ON")

    tempReadings = fastReadings

    for i in range(len(tempReadings)):

        currentTemp  = tempReadings[i]

        if currentTemp > hotTemp:

            state = "Hot (AC On)"
            speed = int(5*currentTemp + 50)

            #turn left for AC
            board.pwm_write(pin1A, 0)
            board.pwm_write(pin2A, speed)


        elif currentTemp < coldTemp:

            state = "Cold (Heat On)"
            speed = int(-5*currentTemp + 300)

            # turn right for heater
            board.pwm_write(pin1A, speed)
            board.pwm_write(pin2A, 0)

        else:

            state = "Room (Fan Off)"
            speed = 0
            board.pwm_write(pin1A, 0)
            board.pwm_write(pin2A, 0)

        print(f"{get_timestamp()} - Temp: {currentTemp} \t State: {state} \t Speed: {speed}")

        time.sleep(1)

    shutdown_motor(board)
    print(f"{get_timestamp()} - Motor: OFF")

    return
