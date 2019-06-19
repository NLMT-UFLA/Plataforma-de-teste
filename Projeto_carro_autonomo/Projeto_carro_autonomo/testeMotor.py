from board import Board
import time

arduino = Board()

pin_6 = arduino.board.get_pin('d:6:p')
pin_11 = arduino.board.get_pin('d:11:p')

pin_11.write(0)
pin_6.write(1)
print("Enviando")

time.sleep(20)
print("Terminou")
pin_11.write(0)
pin_6.write(0)
