# debug mode for testing without led connection
debug = True

if not debug:
    import neopixel
    import board    

import time
import numpy as np

class Kasten:
    ''' Class object for the ledKasten Display '''
    numberOfPixels = 10
    pixels = []
    neopixel_pixels = []
    debug = False
    
    def __init__(self, pixelNumber, debugMode):
        ''' pixelNumber ... number of LEDs in the display array
        debugMode ... True for use without LEDs connected '''
        self.numberOfPixels = pixelNumber
        self.pixels = [(0,0,0)] * pixelNumber
        self.debug = debugMode
        
        # create the neopixel object
        if debug:
            self.neopixel_pixels = self.pixels
        else:
            self.neopixel_pixels = neopixel.NeoPixel(board.D18, self.numberOfPixels)
        
    def sync(self):
        ''' Synchronize the screen '''
        self.neopixel_pixels = self.pixels
        
    def setPixel(self, x, y, col):
        ''' Set a pixel on the matrix
        x,y ... position
        col ... 3-touple for (r,g,b) '''
        print(x)
        self.mapping = [[ 1.,  8.,  9., 16., 17., 24., 25., 32., 33., 40.],
                        [ 2.,  7., 10., 15., 18., 23., 26., 31., 34., 39.],
                        [ 3.,  6., 11., 14., 19., 22., 27., 30., 35., 38.],
                        [ 4.,  5., 12., 13., 20., 21., 28., 29., 36., 37.]]
        
        i = int(self.mapping[x][y] - 1)
        self.pixels[i] = col
        
kasten = Kasten(40, True)

def __main__():
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
                        kasten.setPixel(x, y, (r1, g1, b1))
                    else:
                        kasten.setPixel(x, y, (r2, g2, b2))
                if count == 1:
                    kasten.setPixel(x, y, (r1, g1, b1))
                if count == 2:
                    if x == m or x == n:
                        kasten.setPixel(x, y, (r2, g2, b2))
                    else:
                        kasten.setPixel(x, y, (r1, g1, b1))
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
            
        kasten.sync()

__main__()





