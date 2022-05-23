import time
import math
from pymata4.pymata4 import Pymata4

from modules.file import get_system_parameter

thermistorPin = int(get_system_parameter(name="THERMISTOR"))
R1            = 100000
tempReadings  = []


def setup_thermistor(board: Pymata4):

    """A function to set up thermistor"""

    board.set_pin_mode_analog_input(thermistorPin)

    return


def get_temp(board: Pymata4):

    """A function to return temperature readings"""

    Vo = board.analog_read(thermistorPin)[0]
    R2 = R1*((1023 / Vo) - 1)
    temp = -21.21*math.log(R2/1000)+72.203
    tempReadings.append(temp)

    return tempReadings
