import serial
import time

ser = serial.Serial('/dev/ttyACM1',9600)

class Receptor:
        def __init__(self):
                self.data = ser.readline()
                
        def atualizaDados(self):
                self.data = ser.readline()
                x,y,f = self.data.split(';')

        def getX(self):
                x,y,f = self.data.split(';')
                return x
        
        def getY(self):
                x,y,f = self.data.split(';')
                return y
        
        def getF(self):
                x,y,f = self.data.split(';')
                return f


        
