# Description: Code for ultrasonic sensor
# Author: C20
# Notes:
# - Week 7 Practical
# - Potentially use for safety

import time
from pymata4.pymata4 import Pymata4

from modules.console  import get_timestamp, ask_user
from modules.file     import get_system_parameter
from modules.plotting import plot_graph, save_graph


logs = []
distances = []

def run_sonar(board: Pymata4, x: int):

    triggerPin = int(get_system_parameter(name="TRIGGER"))
    echoPin    = int(get_system_parameter(name="ECHO"))

    """A function that uses the ultrasonic sensor for x seconds to measure the distance of an object in cm """

    endTime = time.time() + x

    board.set_pin_mode_sonar(triggerPin, echoPin, callback=lambda data: logs.append(data), timeout=200000)

    print(f"{get_timestamp()} - Ultrasonic Sensor: ON")

    while time.time() < endTime:

        time.sleep(1)

        distance = logs[-1][2]
        distances.append(distance)

        print(f"{get_timestamp()} - Distance: {distance} cm")

    print(f"{get_timestamp()} - Ultrasonic Sensor: OFF")

    response = ask_user("Plot data (y/n)")
    if response is True:

        times = [s for s in range(1, len(distances)+1)]
        plot_graph(
            times, distances, '.',
            title = "Ultrasonic Sensor", xLabel = "time (s)", yLabel = "distance (cm)",
            grid = True
        )

        response = ask_user("Save graph (y/n)")
        if response is True:
            save_graph(filename="Ultrasonic Sensor")

    return
