import neopixel
import board
import time
import numpy as np



numberOfPixels = 41

pixels = neopixel.NeoPixel(board.D18, numberOfPixels)
x = 0
y = 0

def setPixel(x, y, g, r, b):
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
	height = 11
	X = np.zeros((4, 11), dtype=bool)
	r = int(np.random.rand() * 255)
	g = int(np.random.rand() * 255)
	b = int(np.random.rand() * 255)
	rOld = 0
	gOld = 0
	bOld = 0
	while True:
		X[0][0] = np.random.choice([True, False])
		X[1][0] = np.random.choice([True, False])
		X[2][0] = np.random.choice([True, False])
		X[3][0] = np.random.choice([True, False])
		for y in range(height):
			for x in range(4):
				r = int(np.random.rand() * 255)
				g = int(np.random.rand() * 255)
				b = int(np.random.rand() * 255)
				if X[x][y]:
					setPixel(x, y, g, r, b)
					if y < 10:
						X[x][y+1] = True
					if y != 0:
						X[x][y-1] = False
						setPixel(x, y-1, gOld, rOld, bOld)
					if y == height-1 and x == 0:
						if X[x][y] and X[x+1][y] and X[x+2][y] and X[x+3][y]:
							height -= 1
					time.sleep(0.05)
		if height == 0:
			rOld = r
			gOld = g
			bOld = b
			r = int(np.random.rand() * 255)
			g = int(np.random.rand() * 255)
			b = int(np.random.rand() * 255)
			height = 11





__main__()
