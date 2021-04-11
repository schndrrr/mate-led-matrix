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


def life_step(X):
    """Game of life step using generator expressions"""
    nbrs_count = sum(np.roll(np.roll(X, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    time.sleep(0.3)
    return (nbrs_count == 3) | (X & (nbrs_count == 2))

def __main__():
#pixels[0] = (255, 0, 0)
	X = np.zeros((4, 10), dtype=bool)
	r = np.random.random((4, 10))
	X = (r > 0.75)
	deadcount = 0
	alivecount = 0
	toLongDead = 0
	toLongAlive = 0
	while True:
		X = life_step(X)
		r = int(np.random.rand() * 255)
		g = int(np.random.rand() * 255)
		b = int(np.random.rand() * 255)
		for x in range(4):
			for y in range(10):
				if X[x][y]:
					setPixel(x, y, r, g, b)
					alivecount += 1
				else:
					setPixel(x, y, 0, 0, 0)
					deadcount += 1
		if deadcount == 40:
			toLongDead += 1
		
		toLongAlive +=1

		if toLongDead < 1:
			X = np.zeros((4, 10), dtype=bool)
			r = np.random.random((4, 10))
			X = (r > 0.75)
			toLongDead = 0
		if toLongAlive == 100:
			X = np.zeros((4, 10), dtype=bool)
			r = np.random.random((4, 10))
			X = (r > 0.75)
			toLongAlive = 0




__main__()
