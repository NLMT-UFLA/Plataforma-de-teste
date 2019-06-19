from board import Board
import time
import pyfirmata
from pyfirmata.util import Iterator
import threading 

class Potenciometro(threading.Thread):

    def _init_(board, pin):
        self.arduino = board
        self.iterator = Iterator(arduino.board)
        pin_config = 'a:' + pin + ':i'
        a = arduino.board.get_pin(pin_config)
        a.enable_reporting()

        self.valor = 0

    def run(self):

        while(True):
            
            self.iterator.start()
            
            self.valor = a.read()
            self.arduino.board.pass_time(1)
            time.sleep(0.5)

    def getPotValue(self):
        return self.valor