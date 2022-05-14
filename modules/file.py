# Description: Code for reading and writing to text file
# Author: C20
# Notes:
# - Block 5 - Security


def get_system_parameter(name: str):

    """A function that retrieves the current value of a system parameter stored in parameters.txt"""

    file = open('parameters.txt', 'r')
    parameters = file.readlines()

    for parameter in parameters:
        if parameter.startswith(name):
            value = parameter.split(" = ")[1].strip('\n')

    file.close()

    return value


def update_system_parameter(name: str, value: str):

    """A function that updates the value of a system parameter stored in parameters.txt"""

    file = open('parameters.txt', 'r')
    parameters = file.readlines()

    for i in range(0, len(parameters)):
        parameter = parameters[i]
        if parameter.startswith(name):
            parameters[i] = f"{name} = {value}\n"

    file = open('parameters.txt', 'w')
    file.writelines(parameters)

    file.close()

    return
