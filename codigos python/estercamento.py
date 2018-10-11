#-*- coding: utf-8 -*-
import time
import pyfirmata
from pyfirmata import Arduino, util, serial, time

controlePWM = 0
erro = 0
R = 5500

#Interacão do Arduino com o Raspberry via a biblioteca pyFirmata
board = Arduino("/dev/ttyACM0") #porta que o Arduino está conectada no Raspberry
pin_leitura = board.analog[0]

it = pyfirmata.util.Iterator(board)
it.start()
pin_leitura.enable_reporting()


pwm = 1

pin_out = board.get_pin('d:5:p') #Escolhe o pino digital 5~ do Arduino para saída
pin_in = board.get_pin('d:6:p')  #Escolhe o pino digital 6~ do Arduino para entrada


def my_map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

class Estercamento:
    
    def girarHorario(self, controlePWM): #Método que faz o motor girar no sentido horário
        pin_in.write(0)
        pin_out.write(pwm)

    def girarAntiHorario(self, controlePWM): #Método que faz o motor girar no sentido anti-horário
        pin_in.write(pwm)
        pin_out.write(0)
        
    def lerPot(self):
        leitura = pin_leitura.read()

        if leitura != None:
            leitura = leitura*1023
            Vx = (5.0*leitura)/1023.0                    
            resultado = ((5*R)/Vx) - R

            resultado = round(resultado, 2)
            
            return resultado
        pass

    def estercar(self, entrada): #Método que faz chegar na posição desejada via controle PID (Informar o valor entre 0.0 e 1.0 - Equivalem a 0º e 300º)
        valorAnalogico = self.lerPot() #Leitura do valor do potenciometro
        if valorAnalogico > 4200:            
            if entrada > 0:
                self.girarHorario(entrada/100)
                time.sleep(0.1)
        if valorAnalogico < 5200:
            if entrada < 0:
                self.girarAntiHorario(entrada/100)
                time.sleep(0.1)
                        
        
    
