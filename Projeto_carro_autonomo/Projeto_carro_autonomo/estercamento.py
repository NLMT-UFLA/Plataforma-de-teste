import time
import pyfirmata
from pyfirmata.util import Iterator
from board import Board
from Potenciometro import Potenciometro

arduino = Board()

a = arduino.board.get_pin('a:1:i')

in1 = arduino.board.get_pin('d:4:o')
in2 = arduino.board.get_pin('d:8:o')
#pinVel = arduino.board.get_pin('d::o')

class Estercamento:

    def __init__(self):
        self.estercar = 0.0
        self.Pot = Potenciometro(arduino, 1)
        self.Pot.start()
        pass
    
    def direita(self):
        in1.write(0)
        in2.write(1)
        print("Direita")

    def esquerda(self):
        in1.write(1)
        in2.write(0)
        print("Esquerda")

    def parar(self):
        in1.write(1)
        in2.write(1)

    def eixoLivre(self):
        in1.write(0)
        in2.write(0)

    def maP(self, x, x1, x2, y1, y2):
        A = (y1-y2)/(x1-x2)
        B = (y1 - A*x1)
        Y = A*x + B
        return Y

    def setVel(self, vel):
        #pinVel.write(vel)
        pass

    def estercar(self, pos):      
        valorPot = self.Pot.getPotValue()
        print("ValorPot:" + str(valorPot))
        
        pos = self.maP(pos, -63.0, 100.0, 1.0, -1.0)
        print("Setpoint:" + str(pos))
        
        erro = pos - valorPot

        if (erro<=0.1)and(erro>=-0.1):
            erro = 0
        
        if (erro > 0):
            self.direita()
            
        if (erro < 0):
            self.esquerda()

        time.sleep(0.5)