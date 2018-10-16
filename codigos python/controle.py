from carro import Carro
from teclado import Comandos
from receptor import Receptor
from freio import Freio
class Controle:
    def __init__(self):
        self._freio = Freio()
    string = [a,b]
    def control(self, 'string'): #Usar um dicionario para executar comandos
        return{
            'a':self._freio,
            'b':2,
        }[string]