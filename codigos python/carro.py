#!/usr/bin/env python
#-*- coding: utf-8 -*-

#importa classes para cada elemento do veículo
from estercamento import Estercamento
from freio import Freio
from motor import Motor
from ultrassonico import Ultrassonico
from mpu import MPU

class Carro:    
    def __init__(self):    #Construtor da Classe Carro: instancia os objetos de interesse
        self._estercamento = Estercamento()
        self._freio = Freio()
        self._motor = Motor()
        self._ultrassonico = Ultrassonico()
        self._mpu = MPU()
