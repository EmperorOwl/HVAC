# Description: File to store large variables and data
# Author: C20

# ENCODING FOR SHIFT REGISTER TO OUTPUT TO 7-SEG DISPLAY
charLookup = {
    ' ': '0000000',
    '0': '1111110',
    '1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
    '6': '1011111',
    '7': '1110000',
    '8': '1111111',
    '9': '1111011',
    'A': '1110111',
    'a': '1111101',
    'b': '0011111',
    'C': '1001110',
    'c': '0001101',
    'd': '0111101',
    'E': '1001111',
    'F': '1000111',
    'G': '1011110',
    'H': '0110111',
    'h': '0010111',
    'I': '0000110',
    'J': '0111100',
    'L': '0001110',
    'n': '0010101',
    'O': '1111110',
    'o': '0011101',
    'P': '1100111',
    'q': '1110011',
    'r': '0000101',
    'S': '1011011',
    't': '0001111',
    'U': '0111110',
    'u': '0011100',
    'y': '0111011'
}


# OLD FAKE THERMISTOR DATA FOR TESTING MOTOR IN BLOCK 3
coldReadings = [30, 28, 26, 24, 22, 20] + \
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

heatReadings = [20, 22, 24, 26, 28, 30] + \
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

fastReadings = [31 for i in range(1)] + \
               [33 for i in range(2)] + \
               [35 for i in range(3)] + \
               [37 for i in range(4)] + \
               [40 for i in range(5)]
