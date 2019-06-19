# -*- coding: utf-8 -*-
import time
from board import Board

#O presente trabalho se trata de uma simulação
#Os sensores aqui utilizados podem não corresponder aos modelos/versões empregadas no projeto final
#Elementos pertencentes a fases anteriores do projeto encontram-se comentados para possível futura implementação

arduino = Board(); #Define o caminho para o arduíno a ser controlado (deve ser alterado)

#Define as constantes e variáveis globais do projeto

pin_6 = arduino.board.get_pin('d:6:p')
pin_11 = arduino.board.get_pin('d:11:p')



 #configura a variavel de pwm a ser utilizada para controle do motor

#declara a classe motor

class Motor:

    # declarando e iniciando as variáveis utilizadas
    def __init__ (self):
        #ao iniciar a rotina, "liga o motor" em 0%
        self.porcentagemMotor = 0.0
        self.direcaoAtual = "Parado"
        self.setPoint = 0.0
        self.setPointAnterior = 0.0

    def frente(self):
        self.direcaoAtual = "Frente"
        self.acionaMotor()

    def re(self):
    	if(self.direcaoAtual == "Frente"):
            self.pararLentamente()
        
        self.direcaoAtual = "Re"
        
        self.acionaMotor()

    def calculaPorcentagem(self):
        setPointConvertido = abs(self.setPoint)/100.00
        
        if(setPointConvertido>self.porcentagemMotor):
            self.porcentagemMotor = self.porcentagemMotor + 0.05
        elif(setPointConvertido<self.porcentagemMotor):
            self.porcentagemMotor = self.porcentagemMotor - 0.05
        
    def acelerar(self, novoSetPoint):
    	self.setPointAnterior = self.setPoint
    	self.setPoint = novoSetPoint

        if(novoSetPoint> 5):
            self.frente()
        elif(novoSetPoint < -5):
            self.re()
        else:
            self.pararLentamente()

    def pararLentamente(self):
    	if(self.porcentagemMotor > 0.1):
            if(self.direcaoAtual == "Frente"):
                self.acelerar(10)
                self.pararLentamente()
            elif(self.direcaoAtual == "Re"):
                self.acelerar(-10)
                self.pararLentamente()

    def checaLimites(self):
        if(self.porcentagemMotor>1):
            self.porcentagemMotor = 1
        if(self.porcentagemMotor<0):
            self.porcentagemMotor = 0

    def acionaMotor(self):
    	self.checaMudancaBrusca()
    	self.calculaPorcentagem()
        self.checaLimites()

    	if(self.direcaoAtual == "Frente"):
    		pin_11.write(self.porcentagemMotor)
        	pin_6.write(0)
        	print(self.direcaoAtual + ": " + str(self.porcentagemMotor*100)
                      + "  setPoint: " + str(self.setPoint))
        else:
        	pin_6.write(self.porcentagemMotor)
        	pin_11.write(0)
        	print(self.direcaoAtual + ": " + str(self.porcentagemMotor*100)
                      + "  setPoint: " + str(self.setPoint))

        time.sleep(0.3)

    def checaMudancaBrusca(self):
    	diferenca = self.setPoint - self.setPointAnterior
    	if(diferenca> 10): 
    		self.setPoint = self.setPointAnterior + 10
    	elif(diferenca<-10):
    		self.setPoint = self.setPointAnterior - 10

    def desligar(self):
        pin_6.write(0)
        pin_11.write(0)
    


