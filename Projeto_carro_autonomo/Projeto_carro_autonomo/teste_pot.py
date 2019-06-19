import pyfirmata
import time
from pyfirmata.util import Iterator
from board import Board

arduino = Board()
a = arduino.board.get_pin('a:0:i')
a.enable_reporting()


while(True):
    iterator = Iterator(arduino.board)
    iterator.start()
    
    valor = a.read()
    print(str(valor))
    arduino.board.pass_time(1)
