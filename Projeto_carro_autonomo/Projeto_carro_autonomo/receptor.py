import serial
import time
import requests as req

class Receptor:
        def __init__(self):
                self.data = req.get("http://192.168.0.107")
                
        def atualizaDados(self):
                self.data = req.get("http://192.168.0.107")

        def getX(self):
                x,y,f = self.data.text.split(';')
                return int(x)
        
        def getY(self):
                x,y,f = self.data.text.split(';')
                return int(y)
        
        def getF(self):
                x,y,f = self.data.text.split(';')
                return f


                
