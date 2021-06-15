from math import floor
from constants import FORMAT

from Utils.image import decToHex
        




def verticalGradient(c1, c2, w, h, out):
    vFile = open(f'Output\{out}', 'w')
    vFile.truncate()
    result = c1[:]
    f = w - 1

    for column in range(w):
        for row in range(h):
            result[0] = c1[0] + column * (c2[0] - c1[0]) // f
            result[1] = c1[1] + column * (c2[1] - c1[1]) // f
            result[2] = c1[2] + column * (c2[2] - c1[2]) // f

            pixel = f'{result[0]:03}{result[1]:03}{result[2]:03}'
            pixel = decToHex(pixel)
            vFile.write(pixel + FORMAT)

    vFile.close()
    print('Vertical Gradient File Success')


def horizontalGradient(c1, c2, w, h, out):
    vFile = open(f'Output\{out}', 'w')
    vFile.truncate()
    result = c1[:]
    f = w - 1

    for row in range(h):
        for column in range(w):
            result[0] = c1[0] + column * (c2[0] - c1[0]) // f
            result[1] = c1[1] + column * (c2[1] - c1[1]) // f
            result[2] = c1[2] + column * (c2[2] - c1[2]) // f

            pixel = f'{result[0]:03}{result[1]:03}{result[2]:03}'
            pixel = decToHex(pixel)
            vFile.write(pixel + FORMAT)

    vFile.close()
    print('Horizontal Gradient File Success')

def diagonalGradient(c1, c2, w, h, out):
    vFile = open(f'Output\{out}', 'w')
    diagonalArray = []
    vFile.truncate()
    result = c1[:]

    diagonal = h + w
    f = diagonal - 1

    for row in range(h):
        for column in range(w):
            
            diag = column + row
            result[0] = c1[0] + diag * (c2[0] - c1[0]) // f
            result[1] = c1[1] + diag * (c2[1] - c1[1]) // f
            result[2] = c1[2] + diag * (c2[2] - c1[2]) // f
            
            pixel = f'{result[0]:03}{result[1]:03}{result[2]:03}'
            pixel = decToHex(pixel)
            vFile.write(pixel + FORMAT)

    vFile.close()
    print('Diagonal Gradient File Success')


def ownGradient(c1, c2, w, h, out):
    vFile = open(f'Output\{out}', 'w')
    vFile.truncate()
    interval = h // 3
    result = c1

    interval_1 = interval * 2

    for row in range(h):
        for i in range(w):
            pixel = f'{result[0]:03}{result[1]:03}{result[2]:03}'
            pixel = decToHex(pixel)
            vFile.write(pixel + FORMAT)

        if(row < interval):
            result = c1
        else:
            if(row < interval_1 ):
                result = c2
            else:
                result = c1

    vFile.close()
    print('Own Gradient File Success')