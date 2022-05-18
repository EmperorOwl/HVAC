import time
import math
from pymata4 import pymata4


thermistorPin = 1
buttonPin = 11

R1 = 100000


board = pymata4.Pymata4()

board.set_pin_mode_analog_input(thermistorPin)

while True:

    time.sleep(1)

    Vo = board.analog_read(thermistorPin)[0]
    R2 = R1*((1023 / Vo) - 1)

    print(f"Resistance: {R2}")

    if R2 != 0:
        temp = -21.21*math.log(R2/1000)+72.203
        print(f"Temp: {temp}")



