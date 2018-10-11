import threading
import time
from carro import Carro
import pygame

def estercar(x):
        meuCarro._estercamento.estercar(x)

def acelerar(y):  
        meuCarro._motor.acelerar(y)
        aceleracao = meuCarro._motor.getPorcentagem()

def frear(f):
        if f != 0:
                meuCarro._freio.setFreio()
                freio = meuCarro._freio.getFreio()
        else:
                freio = meuCarro._freio.getFreio()
                if freio != 0:
                        meuCarro._freio.unsetFreio()
                  


meuCarro = Carro()
y = 0	

pygame.init()

display = pygame.display.set_mode((100,100))
clock = pygame.time.Clock()

y = 0

while True:
	pygame.event.pump()
	keypressed = pygame.key.get_pressed()

	x = 0
	f = 0

	if keypressed[pygame.K_w]:
		if y < 100:
			y = y + 1
			acelerar(y)
	else:
		if y != 0:
			y = y - 1
			acelerar(y)

	if keypressed[pygame.K_a]:
		x = -1
		estercar(x)

	if keypressed[pygame.K_d]:
		x = 1
		estercar(x)

	if keypressed[pygame.K_s]:
		f = 1
		frear(x)

	if keypressed[pygame.K_q]:
		exit()

	clock.tick(400)

	print(x,y,f)
    
