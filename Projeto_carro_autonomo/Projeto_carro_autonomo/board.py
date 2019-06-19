from pyfirmata import Arduino, util, serial, time

class Board:

    def __init__(self):
        self.board = Arduino("/dev/ttyUSB0")
        
