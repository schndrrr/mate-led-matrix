import neopixel
import board
import time
import numpy as np

numberOfPixels = 41

pixels = neopixel.NeoPixel(board.D18, numberOfPixels)
m = 0
x = 2

oneStep = 255 / numberOfPixels
maxStep = 255
step = 0

#pixels[0] = (255, 0, 0)
while True:
	time.sleep(0.1)
	if x == 2:
		g = maxStep
		r = step
		b = step
	elif x == 3:
		r = maxStep
		g = step
		b = step
	elif x == 4:
		b = maxStep
		g = step
		r = step
	# g = max(g, 0)
	# g = min(g, 255)
	# r = max(g, 0)
	# r = min(g, 255)
	# b = max(g, 0)
	# b = min(g, 255)
	# print(r, g, b)
	pixels[m] = (r, g, b)
	if  m == numberOfPixels-1:
		# for i in range(41, -1, -1):
		# 	time.sleep(0.1)
		# 	print(x)
		# 	pixels[i] = (0, 0, 0)
		if x == 4:
			x = 2
		else:
			x += 1
		m = 0
		step = 0
		maxStep = 255
	else:
		m += 1
		step += oneStep
		maxStep -= oneStep
