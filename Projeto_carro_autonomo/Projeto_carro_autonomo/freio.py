#!/usr/bin/python
# -*- coding: utf-8 -*-
# move a servo from a Tk slider - scruss 2012-10-28

from time import sleep
from board import Board
import pyfirmata

# don't forget to change the serial port to suit
arduino = Board();

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(arduino.board)
iter8.start()
 
# set up pin D9 as Servo Output
pino_freio = arduino.board.get_pin('d:5:s')

class Freio:

    def __init__ (self):
        #ao iniciar a rotina, "liga o motor" em 0%
        self.porcentagem = 0
        pino_freio.write(self.valorAngulo(self.porcentagem))
        incremento = 1

    def valorAngulo(self, valor):
        return valor*0.3
    
    def setFreio(self):
        self.porcentagem = self.porcentagem + 1
        pino_freio.write(self.valorAngulo(self.porcentagem))

    def unsetFreio(self):
        self.porcentagem = 0
        pino_freio.write(self.valorAngulo(self.porcentagem))

    def getFreio(self):
        return self.porcentagem
    
        

        

 


