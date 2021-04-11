import neopixel
import board
import time
import numpy as np



numberOfPixels = 41

pixels = neopixel.NeoPixel(board.D18, numberOfPixels)
x = 0
y = 0

def setPixel(x, y, r, g, b):
	i = 0
	if y == 0:
		i = 1+x
	if y == 1:
		i = 8-x
	if y == 2:
		i = 9+x
	if y == 3:
		i = 16-x
	if y == 4:
		i = 17+x
	if y == 5:
		i = 24-x
	if y == 6:
		i = 25+x
	if y == 7:
		i = 32-x
	if y == 8:
		i = 33+x
	if y == 9:
		i = 40-x
	pixels[i] = (r, g, b)

def __main__():
#pixels[0] = (255, 0, 0)
	X = np.zeros((4, 10), dtype=bool)
	r1 = int(np.random.rand() * 255)
	g1 = int(np.random.rand() * 255)
	b1 = int(np.random.rand() * 255)
	r2 = int(np.random.rand() * 255)
	g2 = int(np.random.rand() * 255)
	b2 = int(np.random.rand() * 255)
	m = 0
	n = 3
	count = 0
	colorCount = 0
	while True:
		for x in range(4):
			for y in range(10):
				if count == 0:
					if x == m or x == n:
						setPixel(x, y, r1, g1, b1)
					else:
						setPixel(x, y, r2, g2, b2)
				if count == 1:
					setPixel(x, y, r1, g1, b1)
				if count == 2:
					if x == m or x == n:
						setPixel(x, y, r2, g2, b2)
					else:
						setPixel(x, y, r1, g1, b1)
					count = 0
				else:
					count +=1
		time.sleep(0.05)
		if m == 0:
			m = 1
			n = 2
		else:
			m = 0
			n = 3
		colorCount += 1
		if colorCount == 20:
			print('da')
			r1 = int(100 * (0.5 + 0.5 * np.sin(0.5 + float(colorCount) / 5.0)))
			g1 = int(255 * (0.5 + 0.5 * np.sin(1.0 + 2.0 * float(colorCount % 3))))
			b1 = int(100 * (0.5 + 0.5))
		elif colorCount == 30:
			print('hier')
			r2 = int(np.random.rand() * 255)
			g2 = int(np.random.rand() * 255)
			b2 = int(np.random.rand() * 255)
			colorCount = 0
				

__main__()





