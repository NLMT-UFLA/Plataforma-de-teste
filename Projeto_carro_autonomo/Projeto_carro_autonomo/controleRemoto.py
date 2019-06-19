from carro import Carro
from receptor import Receptor
from board import Board
import time


arduino = Board()

carro = Carro()
receptor = Receptor()


while (True):
    try:
        receptor.atualizaDados()
        x = receptor.getX()
        y = receptor.getY()
        f = receptor.getF()

        
        carro._estercamento.estercar(x)

        #carro._motor.acelerar(y)
       
        
        if(f == "0"):
            #carro._freio.setFreio()
            print("Freando")
        print("****")
        
    except(KeyboardInterrupt):
        print("Ate mais!")
        carro._motor.desligar()
        break
        

    
