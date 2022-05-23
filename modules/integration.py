# Description: Code for integration
# Author: C20
# Notes

import time
from pymata4.pymata4 import Pymata4

from modules.console    import get_timestamp
from modules.file       import get_system_parameter
from modules.thermistor import setup_thermistor, get_temp
from modules.ultra      import setup_sonar, get_distance
from modules.motor      import setup_motor, run_motor, shutdown_motor
from modules.buzzer     import setup_buzzer, sound_buzzer
from modules.button     import setup_button, check_press
from modules.shift      import setup_display, display
from modules.reset      import setup_reset, check_reset

dangerDistance = int(get_system_parameter(name="DANGER"))

def run_HVAC(board: Pymata4):

    """A function to run fully integrated HVAC system"""

    # SETUP ALL COMPONENTS
    setup_thermistor(board)
    setup_sonar(board)
    setup_motor(board)
    setup_buzzer(board)
    setup_button(board)
    setup_reset(board)
    digits, pins = setup_display(board)

    # RUN SYSTEM
    while True:

        time.sleep(1)

        distance = get_distance()

        if distance <= dangerDistance:  # check that user is not too close to fan
            shutdown_motor(board)
            display(board, digits, pins, string="StOP")
            print(f"{get_timestamp()} - DANGER: Object detected {distance} cm from fan.")

        else:  # otherwise, proceed by getting temperature, activating fan and/or buzzer if necessary

            tempReadings = get_temp(board)
            currentTemp  = tempReadings[-1]
            display(board, digits, pins, string=f"{int(currentTemp)}C")
            run_motor(board, currentTemp)

            if len(tempReadings) > 4:
                if currentTemp - tempReadings[-3] > 1:
                    sound_buzzer(board, intensity=150, duration=1.5)
                    print(f"{get_timestamp()} - Rapid Up Temp: High Buzzer Sound Activated")
                elif tempReadings[-3] - currentTemp > 1:
                    sound_buzzer(board, intensity=50, duration=0.5)
                    print(f"{get_timestamp()} - Rapid Down Temp: Low Buzzer Sound Activated")

        if check_press(board) is True:
            print(f"{get_timestamp()} - Emergency Button Pressed: HVAC Switched Off")
            break

        if check_reset(board) is True:
            board.send_reset()
            print(f"{get_timestamp()} - Board has been reset.")
            break

    return
