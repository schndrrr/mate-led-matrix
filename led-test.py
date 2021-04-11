import neopixel
import board
import time
import numpy as np

pixels = neopixel.NeoPixel(board.D18, 50)

#pixels[0] = (255, 0, 0)
while True:
    for t in np.linspace(0., 2.*np.pi, 100):
        time.sleep(0.1)
        for m in range(50): 
            a = int(100 * (0.5 + 0.5 * np.sin(t + 0.5 + float(m) / 5.0)))
            b = int(255 * (0.5 + 0.5 * np.sin(t + 1.0 + 2.0 * float(m % 3))))
            c = int(100 * (0.5 + 0.5 * np.sin(t)))
            pixels[m] = (a, b, c)
