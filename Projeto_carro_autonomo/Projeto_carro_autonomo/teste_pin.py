from board import Board

arduino = Board()
pino = arduino.board.get_pin('d:3:o')
pino.write(1)
