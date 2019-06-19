# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from pyfirmata import Arduino
import mpu6050

board = Arduino('/dev/ttyUSB0')
pinSCL = board.get_pin('d:5:i')
pinSDA = board.get_pin('d:4:i')

class MPU:
    def __init__(self, address):
    	_mpu = mpu6050(address)

    def setRangeAceleracao(self, range):
	    #Passar como parâmetro uma das seguintes constantes:
	    #ACCEL_RANGE_2G     
	    #ACCEL_RANGE_4G
	    #ACCEL_RANGE_8G
	    #ACCEL_RANGE_16G
        self._mpu.set_accel_range(range)
        pass
    
    def getAceleracao(self):
		#Retorna a aceleracao na forma de uma lista, onde a[0] = ax, a[1]= ay e a[2]= az
		#UNIDADE DAS MEDIDAS: [g]
     	a = _mpu.get_accel_data()
     	return [a['x'], a['y'], a['z']]

    def setGyroRange(self, range):
		#Passar como parâmetro uma das seguintes constantes:
		#GYRO_RANGE_250DEG
    	#GYRO_RANGE_500DEG
    	#GYRO_RANGE_1000DEG
    	#GYRO_RANGE_2000DEG
        self._mpu.set_gyro_range(range)
        pass
    
    def getPosicao(self):
		#Retorna a posição na forma de uma lista, onde pos[0] = gx, pos[1]= gy e pos[2]= gz
    	pos= self._mpu.get_gyro_data()
    	return [pos['x'], pos['y'], pos['z']]
	
    def getTemp(self):
    	return self.mpu.get_temp();


sensor = MPU(0x68)
while(1):
    print(sensor.getTemp())
    print

    accel_data = sensor.getAceleracao()
    print "Accel_x: ",
    print accel_data['x']
    print "Accel_y: ",
    print accel_data['y']
    print "Accel_z: ",
    print accel_data['z']
    print

    
    gyro_data = sensor.getPosicao()
    print "Gyro_x: ",
    print gyro_data['x']
    print "Gyro_y: ",
    print gyro_data['y']
    print "Gyro_z: ",
    print gyro_data['z']
    print

    time.sleep(2)
