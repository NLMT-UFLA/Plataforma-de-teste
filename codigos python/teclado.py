import keyboard
import time

y = 0
f = 0

while True:
	x = 0

	if keyboard.is_pressed('esc'):
		print('finish!')
		break

	if keyboard.is_pressed('up'):
		if y < 100:
			y = y + 1
	else:
		if y != 0:
			y = y - 1

	if keyboard.is_pressed('down'):
		if f < 100:
			f = f + 1
	else:
		if f != 0:
			f = f - 1

	if keyboard.is_pressed('left'):
		x = 1

	if keyboard.is_pressed('right'):
		x = 2

	print(x,y,f)

	time.sleep(0.01)


