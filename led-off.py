import neopixel
import board
import time
import numpy as np

pixels = neopixel.NeoPixel(board.D18, 50)

for m in range(50):
    pixels[m] = (0,0,0)

