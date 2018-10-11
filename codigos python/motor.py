# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import pyfirmata
from pyfirmata import Arduino, util
import time

#O presente trabalho se trata de uma simulação
#Os sensores aqui utilizados podem não corresponder aos modelos/versões empregadas no projeto final
#Elementos pertencentes a fases anteriores do projeto encontram-se comentados para possível futura implementação

board = Arduino('/dev/ttyACM0') #Define o caminho para o arduíno a ser controlado (deve ser alterado)

#Define as constantes e variáveis globais do projeto


pin_motor = board.get_pin('d:3:p')
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(23,GPIO.OUT)
#GPIO.setup(DIGITAL_BRAKE,GPIO.OUT)
pin_freio = board.get_pin('d:9:p')
pin_freio.write(0)

 #configura a variavel de pwm a ser utilizada para controle do motor

#declara a classe motor

class Motor:

    # declarando e iniciando as variáveis utilizadas
    def __init__ (self):
        #ao iniciar a rotina, "liga o motor" em 0%
        self.porcentagem_motor = 0.0
        self.freio_motor = 1
        self.aceleracao = 0
        
    def acelerar(self, aceleracao):
        # Altera a porcentagem de giro do motor, de acordo a nova porcentagem desejada
        # Faz isso alterando a tensão do sinal ligado ao controlador do motor, através de um controle pwm

        self.aceleracao = aceleracao/100.0
        print(self.aceleracao)
        pin_motor.write(self.aceleracao)

    def getPorcentagem(self):
        # Retorna a porcentagem de giro atual do motor em relação a seu valor máximo
        return self.porcentagem_motor
    
    def setBrake(self):
        # Desliga o motor sem cortar a alimentação
        self.freio_motor = 1
        pin_freio.write(freio_motor)

    def unsetBrake(self):
        # Desliga o freio_motor
        self.freio_motor = 0
        pin_freio.write(freio_motor)


