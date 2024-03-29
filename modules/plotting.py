# Description: Code for graphing
# Author: C20
# Notes:
# - Week 7 Practical

import time
import matplotlib.pyplot as plt

from modules.console import get_timestamp

fig = plt.gcf()

def plot_graph(x: list, y: list, marker: str, title: str, xLabel: str, yLabel: str, grid: bool):

    """A function to plot graph"""

    plt.plot(x, y, marker)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(grid, linestyle='-', alpha=0.65)

    print(f"{get_timestamp()} - Graph has been plotted. Close plot to continue.")

    plt.show()

    return


def save_graph(filename):

    """A function to save graph."""

    fig.savefig(
        f"plots/{filename} ({time.strftime('%d-%m-%y %H.%M')}).png",
        dpi = 750,  # increase picture quality
    )

    print(f"{get_timestamp()} - Graph has been saved. Head to plots folder to view.")

    return
