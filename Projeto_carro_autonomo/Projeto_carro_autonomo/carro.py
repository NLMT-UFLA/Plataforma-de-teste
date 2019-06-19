#!/usr/bin/env python
#-*- coding: utf-8 -*-

#importa classes para cada elemento do veículo
from estercamento import Estercamento
from freio import Freio
from motor import Motor
import threading

class Carro:    
    def __init__(self):    #Construtor da Classe Carro: instancia os objetos de interesse
        self._estercamento = Estercamento()
        self._freio = Freio()
        self._motor = Motor()
    

                
                
    
